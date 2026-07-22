/*
 * EX.NO: 6E - Serial Communication - LED Control
 * AIM: Control LED via Serial port commands
 * Hardware: Arduino UNO, LED on Pin 4
 * Usage: Open Serial Monitor at 9600 baud
 *        Send '1' -> LED ON
 *        Send '2' -> LED OFF
 */
void setup() {
    Serial.begin(9600);
    pinMode(4, OUTPUT);
    Serial.println("LED Control Ready. Send 1=ON, 2=OFF");
}

void loop() {
    if (Serial.available() > 0) {
        char data = Serial.read();
        Serial.print("Received: ");
        Serial.println(data);

        if (data == '1') {
            digitalWrite(4, HIGH);
            Serial.println("LED ON");
        } else if (data == '2') {
            digitalWrite(4, LOW);
            Serial.println("LED OFF");
        }
    }
}
