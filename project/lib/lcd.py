from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

def show_state(state):
    display.fill(0)
    display.text("State:", 0, 0, 1)
    display.text(state, 0, 20, 1)
    display.show()

