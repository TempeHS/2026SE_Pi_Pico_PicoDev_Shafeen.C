from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

class colorvictim:
    def __init__(self, debug=False):
        self.__debug = debug 
    
    def greenvictim(self, threshold=150):
        data = colourSensor.readRGB()
        red = data['red'] # extract the RGB information from data
        grn = data['green']
        blu = data['blue']
        if self.__debug:
            print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red")
        if grn > red + threshold and grn > blu + threshold: # threshold is essentially just making sure the green value is higher then the rest
            return True
        else:
            return False

