# EX.NO: 9A - IR Sensor Interface with Raspberry Pi Pico
# AIM: Interface IR sensor to detect objects and control buzzer
# Hardware: IR Sensor OUT -> GP15, Buzzer -> GP16

from machine import Pin
from time import sleep

buzzer = Pin(16, Pin.OUT)
ir     = Pin(15, Pin.IN)

print("IR Sensor Ready...")

while True:
    ir_value = ir.value()
    if ir_value == True:      # No object detected (IR not blocked)
        print("No Object Detected - Buzzer OFF")
        buzzer.value(0)
    else:                      # Object detected (IR blocked)
        print("Object Detected! - Buzzer ON")
        buzzer.value(1)
    sleep(0.3)
