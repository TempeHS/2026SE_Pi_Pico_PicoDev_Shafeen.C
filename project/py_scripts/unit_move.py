from machine import Pin, PWM
from move import Move 
from servo import Servo
import time

# create a PWM servo controller (16 - pin Pico)
lhs_servo_pwm = PWM(Pin(16))
rhs_servo_pwm = PWM(Pin(15))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

lhs_servo = Servo(pwm=lhs_servo_pwm)
rhs_servo = Servo(pwm=rhs_servo_pwm)


walking = Move(lhs_servo, rhs_servo, debug=True)
print("Starting the walk...")
walking.forward()
walking.backwards()
walking.left()
walking.right()
walking.stop()
walking.spin()




