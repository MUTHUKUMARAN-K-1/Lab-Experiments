# EX.NO: 12 - IoT Smart Home System using Blynk + Raspberry Pi Pico W
# AIM: Control home devices (LED/Relay) remotely via Blynk mobile app
# Hardware: Raspberry Pi Pico W, LED/Relay on GP16
# Blynk: Add Button widget -> Virtual Pin V0

import time
import network
import BlynkLib
from machine import Pin

# ============ CONFIGURE THESE ============
WIFI_SSID     = "Your_WiFi_SSID"
WIFI_PASSWORD = "Your_WiFi_Password"
BLYNK_AUTH    = "Your_Blynk_Auth_Token"
# =========================================

device = Pin(16, Pin.OUT)    # LED or Relay connected to GP16

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

print("Connecting to WiFi...")
wait = 15
while wait > 0:
    if wlan.status() >= 3:
        break
    wait -= 1
    print(".", end="")
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError("WiFi connection failed")
print(f"\nConnected! IP: {wlan.ifconfig()[0]}")

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Handler for Virtual Pin V0 (Button widget in Blynk)
@blynk.on("V0")
def v0_write_handler(value):
    state = int(value[0])
    if state == 1:
        device.value(1)
        print("Device: ON")
    else:
        device.value(0)
        print("Device: OFF")

print("Smart Home System Ready! Control from Blynk app...")

# Main loop
while True:
    blynk.run()
