from machine import Pin, PWM
from movement import Move
from servo import Servo
from time import sleep

lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))

# Use the same style as in movement.py unless you need custom params
left = Servo(pwm=lh_servo_pwm)
right = Servo(pwm=rh_servo_pwm)

movement = Move(left, right, True)

print("Forwards")
movement.forward()
sleep(1)
print("backward")
movement.backward()
sleep(1)
print("left")
movement.left()
sleep(1)
print("right")
movement.right()
sleep(1)
print("stop")
movement.stop()
sleep(1)