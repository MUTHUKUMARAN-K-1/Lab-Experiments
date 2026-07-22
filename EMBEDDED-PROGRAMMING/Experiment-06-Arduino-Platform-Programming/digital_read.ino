/*
 * EX.NO: 6B - Digital Read - Switch Controlled LED
 * AIM: Read switch state using digitalRead and control LED
 * Hardware: Arduino UNO, LED on Pin 2, Switch on Pin 5 (INPUT_PULLUP)
 */
void setup() {
    pinMode(2, OUTPUT);
    pinMode(5, INPUT_PULLUP);   // Internal pull-up resistor
}

void loop() {
    int switchState = digitalRead(5);
    if (switchState == HIGH) {
        /* Button not pressed - blink LED 5 times */
        for (int i = 0; i < 5; i++) {
            digitalWrite(2, HIGH); delay(500);
            digitalWrite(2, LOW);  delay(500);
        }
    } else {
        /* Button pressed - LED stays OFF */
        digitalWrite(2, LOW);
    }
}
