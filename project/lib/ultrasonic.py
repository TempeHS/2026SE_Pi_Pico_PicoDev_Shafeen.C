from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from machine import Pin, PWM
from PiicoDev_Unified import sleep_ms
from servo import Servo
from move import Move 
import time

rhs_servo_pwm = PWM(Pin(16))
lhs_servo_pwm = PWM(Pin(15))

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])


freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

rhs_servo = Servo(pwm=rhs_servo_pwm)
lhs_servo = Servo(pwm=lhs_servo_pwm)

walking = Move(lhs_servo, rhs_servo, debug=True)

class ultrasonic:
    def __init__(self, lhs_servo, rhs_servo debug=False):
        self.__lhs_servo = lhs_servo  # Left wheel servo
        self.__rhs_servo = rhs_servo  # Right wheel servo
        self.__debug = debug
    def run(self):
        while True:
            print(range_a.distance_mm, range_b.distance_mm)
            time.sleep(1)
            dist_weea = range_a.distance_mm
            dist_woob = range_b.distance_mm
            if dist_weea <= 100 and dist_woob <= 100:
            walking.forward()
            walking.left()
            elif dist_weea <= 100:
            walking.right()
            elif dist_woob <= 100:
            walking.left()
            else:
            walking.backwards()
        
            time.sleep(15)


