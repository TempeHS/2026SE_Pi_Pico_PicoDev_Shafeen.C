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


#start
print("Initizlising")


while True:

    dist_wee = range_a.distance_mm
    dist_woo = range_a.distance_mm

    # Print sensor readings (for debugging purposes)
    print("Distance A (Left):", dist_wee, "mm, Distance B (Right):", dist_woo, "mm")

    if dist_wee <= 100 or dist_woo <= 100:
        print("Obstacle detected! Analyzing...")
        walking.left()
        time.sleep(0.05)
    elif dist_wee <= 100 and dist_woo > 100:
        print("turning right")
        walking.right()
        time.sleep(0.05)
    elif dist_wee < 100 and dist_woo < 100:
        walking.left()
        time.sleep(0.05)
    else:
        walking.forward()
        time.sleep(0.05)
        
        


