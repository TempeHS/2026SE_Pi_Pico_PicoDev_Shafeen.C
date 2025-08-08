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
        self.__lhs_servo = lhs_servo
        self.__rhs_servo = rhs_servo 
        self.__debug = debug

    def forward(self):
        if self.__debug:
            print("Going forward")
        #rwheel
        self.__rhs_servo.set_duty(500)
        #lwheel
        self.__lhs_servo.set_duty(2500)
        time.sleep(2)
        

    def backwards(self):
        if self.__debug:
            print("Going backwards")
        self.__rhs_servo.set_duty(2500)
        self.__lhs_servo.set_duty(500)
        time.sleep(2)

    def left(self):
        if self.__debug:
            print("Turning left")
        self.__rhs_servo.set_duty(2500)
        self.__lhs_servo.set_duty(1500)
        time.sleep(2)


    def right(self):
        if self.__debug:
            print("Turning right")
        self.__rhs_servo.set_duty(500)
        self.__lhs_servo.set_duty(1500)
        time.sleep(2)


    def spin(self):
        if self.__debug:
            print("spinning")
        self.__rhs_servo.set_duty(2500)
        self.__lhs_servo.set_duty(2500)
        time.sleep(2)
    
    def stop(self):
        if self.__debug:
            print("STOP")
        self.__rhs_servo.set_duty(1500)
        self.__lhs_servo.set_duty(1500)
        time.sleep(2)
