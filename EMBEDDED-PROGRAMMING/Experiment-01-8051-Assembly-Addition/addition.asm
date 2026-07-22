; EX.NO: 1 - 8051 Assembly Language Program
; AIM: Perform 8-bit addition of two numbers using Keil simulator

        ORG     0000H           ; Start address

        CLR     C               ; Clear carry flag
        MOV     A, #20H         ; Load first operand (32 decimal = 0x20) into Accumulator
        ADD     A, #21H         ; Add second operand (33 decimal = 0x21)
        MOV     R0, A           ; Store result (0x41 = 65 decimal) in Register R0

LOOP:   SJMP    LOOP            ; Infinite loop (halt)
        END

; Expected Result:
;   20H + 21H = 41H (65 in decimal)
;   Register R0 = 41H
