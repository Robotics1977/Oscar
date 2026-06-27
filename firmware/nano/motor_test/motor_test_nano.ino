/*
 * Oscar - Drive Motor Test (Nano + IBT-2 x2)
 * 
 * Tests both wheelchair drive motors forward and reverse at a safe
 * starting speed. R_EN/L_EN on each IBT-2 are wired to 5V (always enabled).
 *
 * NOTE: Both wheelchair motors have integrated 24V brakes.
 * Brakes must be powered (24V) to release before motors will turn,
 * regardless of what this script commands.
 *
 * Pin Assignments:
 *   Motor 1 (left)  - RPWM: D3   LPWM: D5
 *   Motor 2 (right) - RPWM: D6   LPWM: D11
 */

const int M1_RPWM = 3;
const int M1_LPWM = 5;
const int M2_RPWM = 6;
const int M2_LPWM = 11;

const int TEST_SPEED = 128;   // 0-255, ~50% — safe starting point for unknown motors
const int RUN_TIME_MS = 3000; // how long to run each direction
const int PAUSE_MS = 1000;    // pause between movements

void setup() {
  pinMode(M1_RPWM, OUTPUT);
  pinMode(M1_LPWM, OUTPUT);
  pinMode(M2_RPWM, OUTPUT);
  pinMode(M2_LPWM, OUTPUT);

  stopMotors();

  Serial.begin(9600);
  Serial.println("Oscar drive motor test starting...");
  Serial.println("Confirm 24V brake release before motors will respond.");
  delay(2000);
}

void loop() {
  Serial.println("Forward...");
  forward(TEST_SPEED);
  delay(RUN_TIME_MS);

  Serial.println("Stopping...");
  stopMotors();
  delay(PAUSE_MS);

  Serial.println("Reverse...");
  reverse(TEST_SPEED);
  delay(RUN_TIME_MS);

  Serial.println("Stopping...");
  stopMotors();
  delay(PAUSE_MS);

  Serial.println("Test cycle complete. Halting.");
  while (true) {
    // stop here after one full cycle — comment this block out to loop continuously
  }
}

void forward(int speed) {
  analogWrite(M1_RPWM, speed);
  analogWrite(M1_LPWM, 0);
  analogWrite(M2_RPWM, speed);
  analogWrite(M2_LPWM, 0);
}

void reverse(int speed) {
  analogWrite(M1_RPWM, 0);
  analogWrite(M1_LPWM, speed);
  analogWrite(M2_RPWM, 0);
  analogWrite(M2_LPWM, speed);
}

void stopMotors() {
  analogWrite(M1_RPWM, 0);
  analogWrite(M1_LPWM, 0);
  analogWrite(M2_RPWM, 0);
  analogWrite(M2_LPWM, 0);
}
