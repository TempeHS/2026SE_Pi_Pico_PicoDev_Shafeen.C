from machine import Pin, PWM
from servo import Servo
from time import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from movement import Move

lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))


lh_servo = Servo(pwm=lh_servo_pwm)
rh_servo = Servo(pwm=rh_servo_pwm)

range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

movement = Move(lh_servo, rh_servo, debug=True)

while True:
    distancea = range_a.distance_mm  # Use as property, not method
    distanceb = range_b.distance_mm  # Use as property, not method
       
    if distancea <= 0 or distanceb <= 0:
        print("Invalid reading from ultrasonic sensor")
        sleep_ms(100)
        continue  # Skip this loop

    movement.backward()
    print("Distance A (Left):", distancea, "mm, Distance B (Right):", distanceb, "mm")
    if distancea <= 100 and distanceb <= 99:
        movement.stop()
        sleep_ms(600)
        if distancea > distanceb:
            movement.left()
        elif distanceb > distancea:
            movement.right()
        else:
            movement.left()  
        sleep_ms(600)
    elif distancea <= 100 and distanceb >= 101:
        movement.stop()
        sleep_ms(600)
        movement.right()
        sleep_ms(600)
    elif distancea >= 101 and distanceb <= 99:
        movement.stop()
        sleep_ms(600)
        movement.left()
        sleep_ms(600)
    sleep_ms(100)  

    




