# EX.NO: 8 - Raspberry Pi Pico - Switch Controlled LED
# AIM: Read switch state and control LED accordingly
# Hardware: LED -> GP16, Switch -> GP15

from machine import Pin
from time import sleep

led = Pin(16, Pin.OUT)
sw  = Pin(15, Pin.IN)

while True:
    if sw.value() == True:    # Switch released
        print("Switch: Released - Blinking LED")
        led.value(1); sleep(0.5)
        led.value(0); sleep(0.5)
    else:                      # Switch pressed
        print("Switch: Pressed - LED OFF")
        led.value(0)
        sleep(0.1)
