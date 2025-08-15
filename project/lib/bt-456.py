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
    dist_weea = range_a.distance_mm
    dist_woob = range_b.distance_mm

    print("Distance A:", dist_weea, "mm, Distance B:", dist_woob, "mm")

    if dist_weea <= 100 or dist_woob <= 100:
        print("Obstacle detected! Analyzing...")
        walking.stop()
        time.sleep(0.2)
        
    if dist_weea < dist_woob:
        print("Turning right to avoid obstacle!")
        walking.right()  # Turn right
        time.sleep(0.5)  # Wait for the robot to turn
        walking.backwards()  # Move forward after turning

    if dist_weea < dist_woob:
        print("Turning left to avoid obstacle!")
        walking.left()  # Turn left
        time.sleep(1)  # Allow time for the turn
        walking.backwards()  # Move forward after the turn
    else:
        print("Both sensors are blocked, reversing and trying again!")
        walking.backwards()  # Move backward
        time.sleep(1)  # Reverse for 1 second
        walking.left()  # Turn left after backing up
        time.sleep(1)  # Wait for turn
        walking.forward()  # Move forward after turning


    time.sleep(0.5)
        

            







