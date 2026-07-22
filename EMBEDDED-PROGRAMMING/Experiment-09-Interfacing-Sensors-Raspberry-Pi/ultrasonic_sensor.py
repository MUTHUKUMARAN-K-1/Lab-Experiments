# EX.NO: 9B - Ultrasonic Sensor with Raspberry Pi Pico
# AIM: Measure distance using HC-SR04 and trigger buzzer
# Hardware: TRIG -> GP14, ECHO -> GP15, Buzzer -> GP16

from machine import Pin
import utime

trigger = Pin(14, Pin.OUT)
echo    = Pin(15, Pin.IN)
buzzer  = Pin(16, Pin.OUT)

def measure_distance():
    # Send 10us trigger pulse
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Wait for echo to go HIGH
    while echo.value() == 0:
        signaloff = utime.ticks_us()

    # Wait for echo to go LOW
    while echo.value() == 1:
        signalon = utime.ticks_us()

    # Calculate distance
    time_passed = signalon - signaloff
    distance_cm = (time_passed * 0.0343) / 2
    return distance_cm

print("Ultrasonic Sensor Ready...")

while True:
    dist = measure_distance()
    print(f"Distance: {dist:.2f} cm")

    if dist <= 10:
        buzzer.value(1)     # Object too close
        print("WARNING: Object too close!")
    else:
        buzzer.value(0)

    utime.sleep(0.5)
