# EX.NO: 11 - Cloud Platform Data Logging with Blynk
# AIM: Read temperature from Pico W and upload to Blynk cloud platform
# Hardware: Raspberry Pi Pico W (built-in temperature sensor)
# Prerequisites: pip install blynklib, configure WiFi + Blynk credentials

from machine import ADC
import time
import network

# ============ CONFIGURE THESE ============
WIFI_SSID     = "Your_WiFi_SSID"
WIFI_PASSWORD = "Your_WiFi_Password"
BLYNK_AUTH    = "Your_Blynk_Auth_Token"
# =========================================

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

# Import Blynk after WiFi connected
import BlynkLib
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Built-in temperature sensor (ADC pin 4)
adc = ADC(4)

print("Logging temperature to Blynk...")

while True:
    # Read and convert to Celsius/Fahrenheit
    adc_voltage = adc.read_u16() * (3.3 / 65536)
    temp_c = 27 - (adc_voltage - 0.706) / 0.001721
    temp_f = 32 + (1.8 * temp_c)

    print(f"Temp: {temp_c:.2f}C / {temp_f:.2f}F")

    # Upload to Blynk Virtual Pins
    blynk.virtual_write(3, round(temp_c, 2))   # V3 = Celsius
    blynk.virtual_write(4, round(temp_f, 2))   # V4 = Fahrenheit

    blynk.run()
    time.sleep(5)
