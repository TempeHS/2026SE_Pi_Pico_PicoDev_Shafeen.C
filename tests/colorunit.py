from colorsensor import colorvictim
from time import sleep_ms
from machine import Pin, PWM
from servo import Servo
from movement import Move

lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))
lh_servo = Servo(pwm=lh_servo_pwm)
rh_servo = Servo(pwm=rh_servo_pwm)
movement = Move(lh_servo, rh_servo, debug=True)
    
sensor = colorvictim("green", debug=True)

while True:
    if sensor.greenvictim():
        print("Green detected")
        movement.stop()
    else:
        print("Not the victim")
        movement.backward
    sleep_ms(1000)