from asyncore import write
from pathlib import Path
from turtle import right
import sys
from setuptools import Command


class Parser:
    def __init__(self, path) -> None:

        path = Path(path)
        if path.is_dir():
            self.files = list(map(Path, path.iterdir()))
        else:
            self.files = [path]

        self.openFile()
        self.current = None
        self.math_cmd = ('add', 'sub', 'neg', 'eq',
                         'gt', 'lt', 'and', 'or', 'not')
        # while txt := f.readline().replace(' ', ''):
        #       txt = txt.replace('\n', '')
        #        if not txt:
        #             continue
        #         if txt[0:2] == '//':
        #             continue
        #         if txt.find('//') >= 0:
        #             txt = txt[:txt.find('//')]

        #         self.asm_text.append(txt)

    # def hasMoreCommand(self):
    def openFile(self):
        if self.files:
            self.stream = open(self.files.pop())
            return True
        return False

    def advance(self):

        txt = self.stream.readline()
        if not txt:
            if self.openFile():
                return self.advance()
            return False
        txt = txt.strip()
        if txt.find('//') >= 0:
            txt = txt[:txt.find('//')]

        if not txt:
            return self.advance()
        self.current = txt.split()
        return True

    def commandType(self):
        cmd = self.current[0]
        if cmd in self.math_cmd:
            return 'C_ARITHMETIC'
        if cmd == 'push':
            return 'C_PUSH'
        if cmd == 'pop':
            return 'C_POP'
        if cmd == 'label':
            return 'C_LABEL'
        if cmd == 'goto':
            return 'C_GOTO'
        if cmd == 'if-goto':
            return 'C_IF'

        if cmd == 'function':
            return 'C_FUNCTION'
        if cmd == 'return':
            return 'C_RETURN'
        if cmd == 'call':
            return 'C_CALL'

    def arg1(self):
        return self.current[1]

    def arg2(self):
        return self.current[2]

    def getCmd(self):
        return self.current[0]

    def close(self):
        self.stream.close()


class CodeWriter:
    def __init__(self, path) -> None:
        path = Path(path)
        self.name = path.stem
        self.stream = open(path.with_suffix('.asm'), mode='w')
        # VM初期化

        self.w('@256')
        self.w('D=A')
        self.w('M=0')
        self.w('@SP')
        self.w('M=D')
        self.jump_var = 0

    def w(self, str):
        self.stream.write(str)
        self.stream.write('\n')

    def setFileName(self, path):
        path = Path(path)
        self.name = path.stem

    def writeArithmetic(self, command):
        self.w('@SP')
        self.w('A=M-1')
        # Aはstuckpointer
        self.w('D=M')  # Dにxをpop
        self.w('M=0')

        if command in ('neg', 'not'):
            if command == 'neg':
                self.w('M=-D')
            elif command == 'not':
                self.w('M=!D')

        else:
            # pop 処理

            self.w('A=A-1')
            if command == 'add':
                self.w('M=D+M')
            elif command == 'sub':
                self.w('M=M-D')

            elif command in ('eq', 'gt', 'lt'):
                if command == 'eq':
                    jump = 'JEQ'
                elif command == 'gt':
                    jump = 'JGT'
                elif command == 'lt':
                    jump = 'JLT'
                self.w('D=M-D')
                self.w(f'@JMPVAR{self.jump_var}')
                self.w(f'D;{jump}')

                # falseの場合
                self.w('@SP')
                self.w('A=M-1')
                self.w('A=A-1')
                self.w('M=0')
                self.w(f'@JMPVAR{self.jump_var}RE')
                self.w('0;JMP')
                # trueの場合

                self.w(f'(JMPVAR{self.jump_var})')
                self.w('@SP')
                self.w('A=M-1')
                self.w('A=A-1')
                self.w('M=-1')

                self.w(f'@JMPVAR{self.jump_var}RE')
                self.w('0;JMP')

                # 比較から復帰
                self.w(f'(JMPVAR{self.jump_var}RE)')
                self.jump_var += 1
            elif command == 'and':
                self.w('M=D&M')
            elif command == 'or':
                self.w('M=D|M')
            self.w('@SP')
            self.w('M=M-1')

    def writePushPop(self, command, segment, index):
        if command == 'pop':

            def poptoR14(seg):
                self.w(f'@{seg}')
                self.w(f'AM=M-1')
                self.w(f'D=M')
                self.w(f'@R14')
                self.w(f'M=D')

            def setptoR15(seg):
                self.w(f'@{seg}')
                self.w('D=M')  # base
                self.w(f'@{index}')
                self.w('D=D+A')  # base+i

                self.w('@R15')
                self.w('M=D')

            def push():

                self.w('@R14')
                self.w('D=M')

                self.w('@R15')
                self.w('A=M')

                self.w('M=D')

            poptoR14('SP')

            if segment == 'local':
                setptoR15('LCL')

            elif segment == 'argument':
                setptoR15('ARG')

            elif segment == 'this':
                setptoR15('THIS')
            elif segment == 'that':
                setptoR15('THAT')

            elif segment == 'pointer':
                self.w('@THIS')
                self.w('D=A')
                self.w(f'@{index}')
                self.w('D=D+A')
                self.w('@R15')
                self.w('M=D')

            elif segment == 'temp':
                self.w('@R5')
                self.w('D=A')
                self.w(f'@{index}')
                self.w('D=D+A')
                self.w('@R15')
                self.w('M=D')

            elif segment == 'static':
                self.w(f'@{self.name}.{index}')
                self.w('D=A')
                self.w(f'@R15')
                self.w('M=D')

            else:
                print('error')
            push()

        elif command == 'push':

            def pushD():
                self.w('@SP')
                self.w('A=M')  # A=pointer
                self.w('M=D')

                self.w('@SP')
                self.w('AM=M+1')
                self.w('M=0')

            def push(seg):
                self.w(f'@{seg}')
                self.w('D=M')  # base
                self.w(f'@{index}')
                self.w('A=D+A')  # base+i
                self.w('D=M')  # pop seg[pointer] to D

            if segment == 'local':
                push('LCL')
            elif segment == 'argument':
                push('ARG')

            elif segment == 'this':
                push('THIS')
            elif segment == 'that':
                push('THAT')

            elif segment == 'pointer':
                self.w('@THIS')
                self.w('D=A')
                self.w(f'@{index}')
                self.w('A=D+A')
                self.w('D=M')
            elif segment == 'temp':
                self.w('@R5')
                self.w('D=A')
                self.w(f'@{index}')
                self.w('A=D+A')
                self.w('D=M')

            elif segment == 'static':
                self.w(f'@{self.name}.{index}')
                self.w('D=M')
            elif segment == 'constant':
                self.w(f'@{index}')
                self.w('D=A')
            else:
                print('error')
            pushD()
        else:
            print('error')

    def close(self):
        self.w('@END')
        self.w('0;JMP')
        self.w('(END)')
        self.w('@END')
        self.w('0;JMP')
        self.stream.close()


def main():
    path = sys.argv[1]
    # path = '/Users/yudai/Documents/nand2tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm'
    parser = Parser(path)
    writer = CodeWriter(path)

    try:

        while parser.advance():
            print(parser.getCmd())

            if parser.commandType() == 'C_ARITHMETIC':
                writer.writeArithmetic(parser.getCmd())
            elif parser.commandType() == 'C_PUSH':
                writer.writePushPop('push', parser.arg1(), parser.arg2())

            elif parser.commandType() == 'C_POP':
                writer.writePushPop('pop', parser.arg1(), parser.arg2())

            elif parser.commandType() == 'C_LABEL':
                print('not deploy')
            elif parser.commandType() == 'C_GOTO':
                print('not deploy')
            elif parser.commandType() == 'C_IF':
                print('not deploy')
            elif parser.commandType() == 'C_FUNCTION':
                print('not deploy')
            elif parser.commandType() == 'C_RETURN':
                print('not deploy')
            elif parser.commandType() == 'C_CALL':
                print('not deploy')
    except Exception as e:
        print(e)
    finally:

        parser.close()
        writer.close()


if __name__ == '__main__':
    main()
