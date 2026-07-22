# EX.NO: 8 - Raspberry Pi Pico - RGB LED Control
# AIM: Control RGB LED using three GPIO pins
# Hardware: R -> GP16, G -> GP17, B -> GP18

from machine import Pin
from time import sleep_ms, sleep

r = Pin(16, Pin.OUT)     # Red LED on GP16
g = Pin(17, Pin.OUT)     # Green LED on GP17
b = Pin(18, Pin.OUT)     # Blue LED on GP18

while True:
    # Red
    r.value(1); sleep_ms(1000); r.value(0); sleep_ms(500)
    # Green
    g.value(1); sleep(1);       g.value(0); sleep(0.5)
    # Blue
    b.value(1); sleep(1);       b.value(0); sleep(0.5)
