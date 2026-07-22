/*
 * EX.NO: 6C - Analog Read - Joystick to LED
 * AIM: Read joystick analog value and control LED
 * Hardware: Arduino UNO, LED on Pin 2, Joystick VRx on A0
 */
void setup() {
    pinMode(2, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int joystickValue = analogRead(A0);  // Read joystick (0-1023)
    Serial.print("Joystick: ");
    Serial.println(joystickValue);

    if (joystickValue > 800) {
        digitalWrite(2, HIGH);  // LED ON if joystick pushed right
    } else {
        digitalWrite(2, LOW);   // LED OFF otherwise
    }
    delay(200);
}
