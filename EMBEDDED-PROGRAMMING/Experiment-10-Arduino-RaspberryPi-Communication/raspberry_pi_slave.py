# EX.NO: 10 - Raspberry Pi Pico (Slave) - Receives from Arduino
# AIM: Receive Bluetooth data from Arduino and control LED
# Hardware: UART0 RX=GP0, TX=GP1, LED=GP16

from machine import Pin, UART

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
led  = Pin(16, Pin.OUT)

print("Raspberry Pi Pico: Waiting for commands...")

while True:
    if uart.any() > 0:
        data = uart.read(1)      # Read 1 byte
        if data:
            cmd = data.decode('utf-8').strip()
            print(f"Received: {cmd}")

            if 'A' in cmd:
                led.value(1)
                print("LED ON")
                uart.write("LED ON\n")
            elif 'B' in cmd:
                led.value(0)
                print("LED OFF")
                uart.write("LED OFF\n")
