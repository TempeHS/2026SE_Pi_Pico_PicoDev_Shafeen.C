from machine import Pin, PWM
from servo import Servo
from time import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from colorsensor import colorvictim
from movement import Move
from lcd import show_state


lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))
lh_servo = Servo(pwm=lh_servo_pwm)
rh_servo = Servo(pwm=rh_servo_pwm)
range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
movement = Move(lh_servo, rh_servo, debug=True)
sensor = colorvictim("green", debug=True)

def navigation():
    while True:
        distancea = range_a.distance_mm
        distanceb = range_b.distance_mm

        if sensor.greenvictim():
            show_state("Green dectected")
            print("Green victim detected!") # helps with debugging
            movement.stop() # stops when it sees the green AH OH
            sleep_ms(1000) # let it snooze
            continue # skips the loop
            
        movement.backward()
        show_state("backward")
        print("Distance A (Left):", distancea, "mm, Distance B (Right):", distanceb, "mm")
        if distancea <= 100 and distanceb <= 99:
            movement.stop()
            show_state("stop")
            sleep_ms(600)
            if distancea > distanceb:
                movement.left()
                show_state("left")
            elif distanceb > distancea:
                movement.right()
                show_state("right")
            else:
                movement.left()
                show_state("left")  
            sleep_ms(600)
        elif distancea <= 100 and distanceb >= 101:
            movement.stop()
            show_state("stop")
            sleep_ms(600)
            movement.right()
            show_state("right")
            sleep_ms(600)
        elif distancea >= 101 and distanceb <= 99:
            movement.stop()
            show_state("stop")
            sleep_ms(600)
            movement.left()
            show_state("left")
            sleep_ms(600)
        sleep_ms(100)

navigation()



