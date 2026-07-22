/*
 * EX.NO: 6D - Analog Write - LED Fade using PWM
 * AIM: Control LED brightness using analogWrite (PWM)
 * Hardware: Arduino UNO, LED on PWM Pin 3
 */
void setup() {
    pinMode(3, OUTPUT);
}

void loop() {
    /* Fade in */
    for (int brightness = 0; brightness <= 255; brightness++) {
        analogWrite(3, brightness);
        delay(10);
    }
    /* Fade out */
    for (int brightness = 255; brightness >= 0; brightness--) {
        analogWrite(3, brightness);
        delay(10);
    }
}
