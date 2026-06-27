"""
Oscar - Drive Motor Test (Raspberry Pi 3B+ via RPi.GPIO)
ARCHIVED - superseded by firmware/nano/motor_test/motor_test_nano.ino

Originally used for the first spin test of the wheelchair drive motors
via two IBT-2 drivers, before the project moved motor control to a
dedicated Arduino Nano (frees up the Pi, keeps E-stop/motor control
independent of the main compute board).

Pin Assignments (BCM numbering):
  Motor 1 - RPWM: GPIO18   LPWM: GPIO13
  Motor 2 - RPWM: GPIO12   LPWM: GPIO19

NOTE: Both wheelchair motors have integrated 24V brakes.
Brakes must be powered (24V) to release before motors will turn.
"""

import RPi.GPIO as GPIO
import time

# Pin definitions
RPWM_1 = 18  # Motor 1 forward PWM
LPWM_1 = 13  # Motor 1 reverse PWM
RPWM_2 = 12  # Motor 2 forward PWM
LPWM_2 = 19  # Motor 2 reverse PWM

GPIO.setmode(GPIO.BCM)
GPIO.setup(RPWM_1, GPIO.OUT)
GPIO.setup(LPWM_1, GPIO.OUT)
GPIO.setup(RPWM_2, GPIO.OUT)
GPIO.setup(LPWM_2, GPIO.OUT)

# Setup PWM at 1000Hz
pwm_r1 = GPIO.PWM(RPWM_1, 1000)
pwm_l1 = GPIO.PWM(LPWM_1, 1000)
pwm_r2 = GPIO.PWM(RPWM_2, 1000)
pwm_l2 = GPIO.PWM(LPWM_2, 1000)

pwm_r1.start(0)
pwm_l1.start(0)
pwm_r2.start(0)
pwm_l2.start(0)


def forward(speed):
    pwm_r1.ChangeDutyCycle(speed)
    pwm_l1.ChangeDutyCycle(0)
    pwm_r2.ChangeDutyCycle(speed)
    pwm_l2.ChangeDutyCycle(0)


def reverse(speed):
    pwm_r1.ChangeDutyCycle(0)
    pwm_l1.ChangeDutyCycle(speed)
    pwm_r2.ChangeDutyCycle(0)
    pwm_l2.ChangeDutyCycle(speed)


def stop():
    pwm_r1.ChangeDutyCycle(0)
    pwm_l1.ChangeDutyCycle(0)
    pwm_r2.ChangeDutyCycle(0)
    pwm_l2.ChangeDutyCycle(0)


try:
    print("Forward...")
    forward(50)  # 50% speed
    time.sleep(3)

    print("Stopping...")
    stop()
    time.sleep(1)

    print("Reverse...")
    reverse(50)
    time.sleep(3)

    print("Stopping...")
    stop()

except KeyboardInterrupt:
    pass

finally:
    stop()
    pwm_r1.stop()
    pwm_l1.stop()
    pwm_r2.stop()
    pwm_l2.stop()
    GPIO.cleanup()
    print("Done")
