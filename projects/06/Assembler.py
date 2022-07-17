# %%
from pathlib import Path
import sys


def get_path():
    cwd = Path(__file__).resolve().parent
    asm = sys.argv[1]
    asm_absolute_path = cwd/asm
    if asm_absolute_path.is_file():
        return asm_absolute_path
    raise Exception


# %%
class Parser:
    def __init__(self, path) -> None:
        self.asm_text = []
        with open(path, mode='r') as f:
            while txt := f.readline().replace(' ', ''):
                txt = txt.replace('\n', '')
                if not txt:
                    continue
                if txt[0:2] == '//':
                    continue
                if txt.find('//') >= 0:
                    txt = txt[:txt.find('//')]

                self.asm_text.append(txt)

        self.next_line_index = 0
        self.now_line = None

    def hasMoreCommands(self) -> bool:
        return True if self.next_line_index < len(self.asm_text) else False

    def advance(self):
        self.now_line = self.asm_text[self.next_line_index]
        self.next_line_index += 1

    def commandType(self):
        if self.now_line[0] == '@':
            self.symbol = self.now_line[1:]
            return 'A_COMMAND'
        elif '=' in self.now_line or ';' in self.now_line:
            if '=' not in self.now_line:
                self.now_line = '='+self.now_line

            if ';' not in self.now_line:
                self.now_line = self.now_line+';'

            spliteq = self.now_line.split('=')
            self.dest = spliteq[0]
            # print(self.now_line)
            self.comp, self.jump = spliteq[1].split(';')

            return 'C_COMMAND'
        elif self.now_line[0] == '(' and self.now_line[-1] == ')':
            self.symbol = self.now_line[1:-1]
            return 'L_COMMAND'
        else:
            print(self.now_line)
            raise Exception


# %%
class Code:
    def __init__(self, parse) -> None:
        self.parser = parse

    def dest(self):
        str = self.parser.dest
        d1 = 0
        d2 = 0
        d3 = 0
        if 'A' in str:
            d1 = 1

        if 'D' in str:
            d2 = 1

        if 'M' in str:
            d3 = 1
        return f'{d1}{d2}{d3}'

    def comp(self):
        str = self.parser.comp

        a = '0'

        if 'M' in str:
            a = '1'
            str = str.replace('M', 'A')
        if '0' == str:
            return a+'101010'
        if '1' == str:
            return a+'111111'

        if '-1' == str:
            return a+'111010'
        if 'D' == str:
            return a+'001100'
        if 'A' == str:
            return a+'110000'

        if '!D' == str:
            return a+'001101'
        if '!A' == str:
            return a+'110001'

        if '-D' == str:
            return a+'001111'
        if '-A' == str:
            return a+'110011'

        if 'D+1' == str:
            return a+'011111'

        if 'A+1' == str:
            return a+'110111'

        if 'D-1' == str:
            return a+'001110'

        if 'A-1' == str:
            return a+'110010'

        if 'D+A' == str:
            return a+'000010'
        if 'D-A' == str:
            return a+'010011'
        if 'A-D' == str:
            return a+'000111'
        if 'D&A' == str:
            return a+'000000'
        if 'D|A' == str:
            return a+'010101'
        raise Exception

    def jump(self):
        str = self.parser.jump

        if str == '':
            return '000'
        if str == 'JGT':
            return '001'
        if str == 'JEQ':
            return '010'
        if str == 'JGE':
            return '011'
        if str == 'JLT':
            return '100'
        if str == 'JNE':
            return '101'
        if str == 'JLE':
            return '110'
        if str == 'JMP':
            return '111'
        raise Exception


# %%
class SymbolTable:
    def __init__(self) -> None:
        self.table = {}
        self.table['SP'] = 0x0000
        self.table['LCL'] = 0x0001
        self.table['ARG'] = 0x0002
        self.table['THIS'] = 0x0003
        self.table['THAT'] = 0x0004
        for i in range(16):
            self.table[f'R{i}'] = i
        self.table['SCREEN'] = 0x4000
        self.table['KBD'] = 0x6000
        self.next_add = 16

    def addEntry(self, symbol, address):
        self.table[symbol] = address

    def add(self, symbol):
        self.table[symbol] = self.next_add
        self.next_add += 1

    def contains(self, symbol):
        return symbol in self.table

    def getAddress(self, symbol):
        return self.table[symbol]


# %%
def main():
    path = get_path()
    parser = Parser(path)
    # print(parser.asm_text)
    code = Code(parser)
    sym = SymbolTable()

    next_address = 0
    while parser.hasMoreCommands():
        parser.advance()
        command_type = parser.commandType()

        if command_type == 'A_COMMAND':
            next_address += 1
        elif command_type == 'C_COMMAND':
            next_address += 1
        elif command_type == 'L_COMMAND':
            if not sym.contains(parser.symbol):
                sym.addEntry(parser.symbol, next_address)

    hack_path = path.with_suffix('.hack')
    parser.next_line_index = 0
    parser.now_line = None
    with open(hack_path, mode='w') as f:
        while parser.hasMoreCommands():
            parser.advance()
            command_type = parser.commandType()

            if command_type == 'A_COMMAND':
                if not parser.symbol.isdecimal():
                    if not sym.contains(parser.symbol):
                        sym.add(parser.symbol)
                    parser.symbol = sym.getAddress(parser.symbol)
                print(parser.symbol)
                f.write(f'0{int(parser.symbol):015b}\n')
            elif command_type == 'C_COMMAND':
                f.write(f'111{code.comp()}{code.dest()}{code.jump()}\n')


# %%
main()
