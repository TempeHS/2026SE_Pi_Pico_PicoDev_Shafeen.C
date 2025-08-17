from machine import Pin, PWM
from servo import Servo
from time import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from colorsensor import colorvictim
from movement import Move
from lcd import show_state


class Controller:
    def __init__(self):
        self.lh_servo_pwm = PWM(Pin(16))
        self.rh_servo_pwm = PWM(Pin(15))
        self.lh_servo = Servo(pwm=self.lh_servo_pwm)
        self.rh_servo = Servo(pwm=self.rh_servo_pwm)
        self.range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
        self.range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
        self.movement = Move(self.lh_servo, self.rh_servo, debug=True)
        self.sensor = colorvictim(debug=True)

    def navigation(self):
        while True:
            distancea = self.range_a.distance_mm
            distanceb = self.range_b.distance_mm
            if self.sensor.greenvictim():
                show_state("Green detected")
                print("Green victim detected!") # helps with debugging
                self.movement.stop() # stops when it sees the green AH OH
                sleep_ms(1000) # let it snooze
                continue # skips the loop  
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

if __name__ == "__main__":
    controller = Controller()
    controller.navigation()
            



