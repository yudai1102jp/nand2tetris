@256
D=A
M=0
@SP
M=D
@3030
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
AM=M-1
D=M
@R14
M=D
@THIS
D=A
@0
D=D+A
@R15
M=D
@R14
D=M
@R15
A=M
M=D
@3040
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
AM=M-1
D=M
@R14
M=D
@THIS
D=A
@1
D=D+A
@R15
M=D
@R14
D=M
@R15
A=M
M=D
@32
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
AM=M-1
D=M
@R14
M=D
@THIS
D=M
@2
D=D+A
@R15
M=D
@R14
D=M
@R15
A=M
M=D
@46
D=A
@SP
A=M
M=D
@SP
AM=M+1
M=0
@SP
AM=M-1
D=M
@R14
M=D
@THAT
D=M
@6
D=D+A
@R15
M=D
@R14
D=M
@R15
A=M
M=D
@THIS
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
AM=M+1
M=0
@THIS
D=A
@1
A=D+A
D=M
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
@THIS
D=M
@2
A=D+A
D=M
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
@THAT
D=M
@6
A=D+A
D=M
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
@END
0;JMP
(END)
@END
0;JMP