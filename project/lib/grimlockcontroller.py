from machine import Pin, PWM
from servo import Servo
from time import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from colorsensor import colorvictim
from movement import Move
from lcd import show_state

#stuff i need i think
lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))
lh_servo = Servo(pwm=lh_servo_pwm)
rh_servo = Servo(pwm=rh_servo_pwm)
range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
movement = Move(lh_servo, rh_servo, debug=True)
display = create_PiicoDev_SSD1306()



while True:
    distancea = self.range_a.distance_mm
    distanceb = self.range_b.distance_mm  
    self.movement.backward()
    show_state("backward")
    print("Distance A (Left):", distancea, "mm, Distance B (Right):", distanceb, "mm")
    if distancea <= 100 and distanceb <= 99:
        self.movement.stop()
        show_state("stop")
        sleep_ms(600)
        if distancea > distanceb:
            self.movement.left()
            show_state("left")
        elif distanceb > distancea:
            self.movement.right()
            show_state("right")
        else:
            self.movement.left()
            show_state("left")  
        sleep_ms(600)
    elif distancea <= 100 and distanceb >= 101:
        self.movement.stop()
        show_state("stop")
        sleep_ms(600)
        self.movement.right()
        show_state("right")
        sleep_ms(600)
    elif distancea >= 101 and distanceb <= 99:
        self.movement.stop()
        show_state("stop")
        sleep_ms(600)
        self.movement.left()
        show_state("left")
        sleep_ms(600)
    sleep_ms(100)









            



