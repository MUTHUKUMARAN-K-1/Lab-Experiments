/*
 * EX.NO: 5 - Arithmetic Programs using Embedded C
 * AIM: Perform ADD, SUB, MUL, DIV operations and output via Ports
 * Target: AT89C51 / AT89C52
 */

#include <REG51.H>

unsigned char a, b;

void main() {
    a = 0x10;       /* a = 16 decimal */
    b = 0x04;       /* b =  4 decimal */

    P0 = a - b;     /* P0 = 12 = 0x0C */
    P1 = a + b;     /* P1 = 20 = 0x14 */
    P2 = a * b;     /* P2 = 64 = 0x40 */
    P3 = a / b;     /* P3 =  4 = 0x04 */

    while (1);      /* Halt */
}

/*
 * Expected Port Values (check in Keil simulator):
 *   P0 = 0x0C  (SUB: 16 - 4 = 12)
 *   P1 = 0x14  (ADD: 16 + 4 = 20)
 *   P2 = 0x40  (MUL: 16 * 4 = 64)
 *   P3 = 0x04  (DIV: 16 / 4 =  4)
 */
