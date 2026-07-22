; EX.NO: 2B - Data Transfer Type II
; Block data transfer using indirect addressing (loop)

        ORG     0000H
        CLR     C
        MOV     R0, #30H        ; Source start address (30H)
        MOV     R1, #40H        ; Destination start address (40H)
        MOV     R7, #06H        ; Number of bytes to transfer = 6

BACK:   MOV     A, @R0          ; Load byte from source address pointed by R0
        MOV     @R1, A          ; Store byte at destination address pointed by R1
        INC     R0              ; Increment source pointer
        INC     R1              ; Increment destination pointer
        DJNZ    R7, BACK        ; Decrement R7, jump to BACK if not zero

LOOP:   SJMP    LOOP
        END

; Result: 6 bytes copied from RAM[30H..35H] to RAM[40H..45H]
