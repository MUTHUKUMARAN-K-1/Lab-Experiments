/*
 * EX.NO: 4 - Basic Programs using Embedded C
 * AIM: Write basic Embedded C program for LED blinking on 8051 (AT89C51)
 * Target: AT89C51 / AT89C52
 * Tool: Keil uVision5
 */

#include <REG51.h>

sbit LED = P2^0;    /* LED connected to Port 2, Pin 0 */

void delay(unsigned int count) {
    unsigned int i, j;
    for (i = 0; i < count; i++)
        for (j = 0; j < 500; j++);
}

void main() {
    while (1) {
        LED = 0;        /* Turn LED ON (active low) */
        delay(100);
        LED = 1;        /* Turn LED OFF */
        delay(100);
    }
}
