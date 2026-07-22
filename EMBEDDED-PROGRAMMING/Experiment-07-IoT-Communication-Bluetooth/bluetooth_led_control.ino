/*
 * EX.NO: 7 - Bluetooth Communication using HC-05
 * AIM: Control LED via Bluetooth (HC-05 module) from a phone
 * Hardware: Arduino UNO, HC-05 BT Module, LED
 * Connections:
 *   BT VCC -> 5V     BT GND -> GND
 *   BT Tx  -> Pin 2  BT Rx  -> Pin 3
 *   LED    -> Pin 4
 * Phone App: Any Bluetooth Terminal App
 *   Send '1' -> LED ON   Send '2' -> LED OFF
 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);  // RX=Pin2, TX=Pin3

void setup() {
    mySerial.begin(9600);
    Serial.begin(9600);
    pinMode(4, OUTPUT);
    Serial.println("Bluetooth LED Control Ready");
}

void loop() {
    if (mySerial.available() > 0) {
        char data = mySerial.read();
        Serial.print("BT Received: ");
        Serial.println(data);

        if (data == '1') {
            digitalWrite(4, HIGH);
            mySerial.println("LED ON");
        } else if (data == '2') {
            digitalWrite(4, LOW);
            mySerial.println("LED OFF");
        }
    }
}
