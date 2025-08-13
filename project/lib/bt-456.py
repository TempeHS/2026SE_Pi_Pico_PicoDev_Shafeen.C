from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from machine import Pin, PWM
from servo import Servo
from move import Move 
import time

range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

rhs_servo_pwm = PWM(Pin(16))
lhs_servo_pwm = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

rhs_servo = Servo(pwm=rhs_servo_pwm)
lhs_servo = Servo(pwm=lhs_servo_pwm)

walking = Move(lhs_servo, rhs_servo, debug=True)
print("Initizlising")

while True:
    dist_wee = range_a.distance_mm
    dist_woo = range_b.distance_mm

    print(range_a.distance_mm, range_b.distance_mm)
    
    if dist_wee <= 35 or dist_woo <= 35:
        walking.stop()
        walking.backwards()
        walking.left()
    else:
        walking.forward()
    time.sleep(5)


