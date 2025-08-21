from machine import Pin, PWM
from servo import Servo
from time import sleep_ms


lh_servo_pwm = PWM(Pin(16))
rh_servo_pwm = PWM(Pin(15))


freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500


# Only create the servo objects you need
lh_servo = Servo(pwm=lh_servo_pwm)
rh_servo = Servo(pwm=rh_servo_pwm)


class Move:
    def __init__(self, lh_servo, rh_servo, debug):
        self.__lh_servo = lh_servo
        self.__rh_servo = rh_servo
        self.__debug = debug

    def forward(self):
        if self.__debug:
            print("forward")
        self.__lh_servo.set_duty(2500)
        self.__rh_servo.set_duty(500)

    def backward(self):
        if self.__debug:
            print("backward")
        self.__lh_servo.set_duty(500)
        self.__rh_servo.set_duty(2500)

    def left(self):
        if self.__debug:
            print("left (45 degrees)")
        self.__lh_servo.set_duty(500)    
        self.__rh_servo.set_duty(500)   
        sleep_ms(500)                    
        self.stop()

    def right(self):
        if self.__debug:
            print("right (45 degrees)")
        
        self.__lh_servo.set_duty(2500)   
        self.__rh_servo.set_duty(2500)  
        sleep_ms(500)                    # 45-degree turn (adjust as needed)
        self.stop()

    def stop(self):
        if self.__debug:
            print("stop")
        self.__lh_servo.stop()
        self.__rh_servo.stop()