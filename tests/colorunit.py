from colorsensor import colorvictim
from time import sleep_ms
    
sensor = colorvictim("green", debug=True)

while True:
    if sensor.greenvictim():
        print("Green detected")
    else:
        print("Not the victim")
    sleep_ms(1000)