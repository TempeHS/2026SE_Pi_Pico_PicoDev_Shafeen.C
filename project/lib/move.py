from machine import Pin, PWM
from servo import Servo
import time

# create a PWM servo controller (16 - pin Pico)
rhs_servo_pwm = PWM(Pin(16))
lhs_servo_pwm = PWM(Pin(15))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

rhs_servo = Servo(pwm=rhs_servo_pwm)
lhs_servo = Servo(pwm=lhs_servo_pwm)

class Move:
    def __init__(self, lhs_servo, rhs_servo, debug=False):
        self.__lhs_servo = lhs_servo  # Left wheel servo
        self.__rhs_servo = rhs_servo  # Right wheel servo
        self.__debug = debug

    def forward(self):
        if self.__debug:
            print("Going forward")
        self.__rhs_servo.set_duty(1000)  # Right wheel forward
        self.__lhs_servo.set_duty(2000)   # Left wheel forward
        time.sleep(2)

    def backwards(self):
        if self.__debug:
            print("Going backwards")
        self.__rhs_servo.set_duty(2000)   # Right wheel backward
        self.__lhs_servo.set_duty(1000)  # Left wheel backward
        time.sleep(2)

    def left(self):
        if self.__debug:
            print("Turning right")
        self.__rhs_servo.set_duty(1500)  # Right wheel forward
        self.__lhs_servo.set_duty(2000)  # Left wheel stop
        time.sleep(2)

    def right(self):
        if self.__debug:
            print("Turning left")
        self.__rhs_servo.set_duty(1500)  # Right wheel stop
        self.__lhs_servo.set_duty(1000)   # Left wheel forward
        time.sleep(2)

    def stop(self):
        if self.__debug:
            print("STOP")
        self.__rhs_servo.set_duty(1500)  # Neutral
        self.__lhs_servo.set_duty(1500)  # Neutral
        time.sleep(2)