# EX.NO: 8 - Raspberry Pi Pico - LED Blink
# AIM: Write MicroPython program to blink LED on GP16
# Tool: Thonny IDE with MicroPython on Raspberry Pi Pico

from machine import Pin
import time

LED = Pin(16, Pin.OUT)   # LED connected to GP16

while True:
    LED.value(1)          # LED ON
    time.sleep(1)         # Wait 1 second
    LED.value(0)          # LED OFF
    time.sleep(1)         # Wait 1 second
