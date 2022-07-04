// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    @SCREEN
    D=A
    @8192

    D=D+A
    @send

    M=D



(LOOP)
    @SCREEN
    D=A
    @now_add
    M=D

    @KBD
    D=M
    @DRAWB
    D;JGT

    @DRAWW
    D;JEQ

    @LOOP
    0;JMP


(DRAWB)

    @now_add
    D=M
    @send
    D=D-M
    @LOOP
    D;JEQ

    @now_add
    A=M
    
    M=-1
    
    @now_add
    M=M+1

    

    @DRAWB
    0;JMP



(DRAWW)

    @now_add
    D=M
    @send
    D=D-M
    @LOOP
    D;JEQ

    @now_add
    A=M
    
    M=0
    
    @now_add
    M=M+1

    

    @DRAWB
    0;JMP
