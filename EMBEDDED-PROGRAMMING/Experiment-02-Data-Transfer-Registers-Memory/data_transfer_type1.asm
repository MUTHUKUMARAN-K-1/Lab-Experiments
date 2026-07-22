; EX.NO: 2A - Data Transfer Type I
; Transfer specific register values to memory locations

        ORG     0000H
        CLR     C
        MOV     R0, #55H        ; Load 55H into R0
        MOV     R1, #6FH        ; Load 6FH into R1
        MOV     A,  R0          ; Move R0 to Accumulator
        MOV     30H, A          ; Store in memory address 30H
        MOV     A,  R1          ; Move R1 to Accumulator
        MOV     31H, A          ; Store in memory address 31H

LOOP:   SJMP    LOOP
        END

; Result: Internal RAM[30H] = 55H, RAM[31H] = 6FH
