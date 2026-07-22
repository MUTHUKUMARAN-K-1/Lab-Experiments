/*
 * EX.NO: 10 - Arduino (Master) - Bluetooth Communication
 * AIM: Send commands to Raspberry Pi Pico via Bluetooth (HC-05)
 * Hardware: Arduino UNO, HC-05 BT Module (Tx=Pin2, Rx=Pin3)
 * Paired with Raspberry Pi Pico (Slave)
 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);  // RX=Pin2, TX=Pin3

void setup() {
    mySerial.begin(9600);
    Serial.begin(9600);
    Serial.println("Arduino Master: Sending BT signals...");
}

void loop() {
    mySerial.write('A');        // Send 'A' - LED ON command
    Serial.println("Sent: A (LED ON)");
    delay(2000);

    mySerial.write('B');        // Send 'B' - LED OFF command
    Serial.println("Sent: B (LED OFF)");
    delay(2000);
}
