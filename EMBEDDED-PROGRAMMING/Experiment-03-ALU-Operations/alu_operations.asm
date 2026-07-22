; EX.NO: 3 - ALU Operations using 8051 Assembly
; AIM: Perform ADD, SUB, MUL, DIV, AND, OR, XOR, NOT operations

        ORG     0000H
        CLR     C

        ;=== ADDITION ===
        MOV     A, #20H
        ADD     A, #21H
        MOV     41H, A          ; Result 41H at mem[41H]

        ;=== SUBTRACTION ===
        CLR     C
        MOV     A, #20H
        SUBB    A, #18H
        MOV     42H, A          ; Result 08H at mem[42H]

        ;=== MULTIPLICATION ===
        MOV     A, #03H
        MOV     B, #04H
        MUL     AB
        MOV     43H, A          ; Lower byte 0CH at mem[43H]
        MOV     44H, B          ; Upper byte 00H at mem[44H]

        ;=== DIVISION ===
        MOV     A, #95H
        MOV     B, #10H
        DIV     AB
        MOV     45H, A          ; Quotient 09H at mem[45H]
        MOV     46H, B          ; Remainder 05H at mem[46H]

        ;=== AND ===
        MOV     A, #25H
        MOV     B, #12H
        ANL     A, B
        MOV     47H, A          ; Result at mem[47H]

        ;=== OR ===
        MOV     A, #25H
        MOV     B, #15H
        ORL     A, B
        MOV     48H, A          ; Result 35H at mem[48H]

        ;=== XOR ===
        MOV     A, #45H
        MOV     B, #67H
        XRL     A, B
        MOV     49H, A          ; Result 22H at mem[49H]

        ;=== NOT (Complement) ===
        MOV     A, #45H
        CPL     A
        MOV     4AH, A          ; Result BAH at mem[4AH]

LOOP:   SJMP    LOOP
        END
