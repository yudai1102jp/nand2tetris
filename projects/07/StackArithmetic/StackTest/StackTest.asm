@256
D=A
M=0
@SP
M=D
@17
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@17
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR0
D;JEQ
@SP
A=M-1
A=A-1
M=0
@JMPVAR0RE
0;JMP
(JMPVAR0)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR0RE
0;JMP
(JMPVAR0RE)
@SP
M=M-1
@17
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@16
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR1
D;JEQ
@SP
A=M-1
A=A-1
M=0
@JMPVAR1RE
0;JMP
(JMPVAR1)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR1RE
0;JMP
(JMPVAR1RE)
@SP
M=M-1
@16
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@17
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR2
D;JEQ
@SP
A=M-1
A=A-1
M=0
@JMPVAR2RE
0;JMP
(JMPVAR2)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR2RE
0;JMP
(JMPVAR2RE)
@SP
M=M-1
@892
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@891
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR3
D;JLT
@SP
A=M-1
A=A-1
M=0
@JMPVAR3RE
0;JMP
(JMPVAR3)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR3RE
0;JMP
(JMPVAR3RE)
@SP
M=M-1
@891
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@892
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR4
D;JLT
@SP
A=M-1
A=A-1
M=0
@JMPVAR4RE
0;JMP
(JMPVAR4)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR4RE
0;JMP
(JMPVAR4RE)
@SP
M=M-1
@891
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@891
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR5
D;JLT
@SP
A=M-1
A=A-1
M=0
@JMPVAR5RE
0;JMP
(JMPVAR5)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR5RE
0;JMP
(JMPVAR5RE)
@SP
M=M-1
@32767
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@32766
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR6
D;JGT
@SP
A=M-1
A=A-1
M=0
@JMPVAR6RE
0;JMP
(JMPVAR6)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR6RE
0;JMP
(JMPVAR6RE)
@SP
M=M-1
@32766
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@32767
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR7
D;JGT
@SP
A=M-1
A=A-1
M=0
@JMPVAR7RE
0;JMP
(JMPVAR7)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR7RE
0;JMP
(JMPVAR7RE)
@SP
M=M-1
@32766
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@32766
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
D=M-D
@JMPVAR8
D;JGT
@SP
A=M-1
A=A-1
M=0
@JMPVAR8RE
0;JMP
(JMPVAR8)
@SP
A=M-1
A=A-1
M=-1
@JMPVAR8RE
0;JMP
(JMPVAR8RE)
@SP
M=M-1
@57
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@31
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@53
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
M=D+M
@SP
M=M-1
@112
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
M=M-D
@SP
M=M-1
@SP
A=M-1
D=M
M=0
M=-D
@SP
A=M-1
D=M
M=0
A=A-1
M=D&M
@SP
M=M-1
@82
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
A=M-1
D=M
M=0
A=A-1
M=D|M
@SP
M=M-1
@SP
A=M-1
D=M
M=0
M=!D
@END
0;JMP
(END)
@END
0;JMP