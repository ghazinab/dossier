import board
import digitalio
import time

RLed = digitalio.DigitalInOut(board.GP14)
RLed.direction = digitalio.Direction.OUTPUT

GLed = digitalio.DigitalInOut(board.GP13)
GLed.direction = digitalio.Direction.OUTPUT

BLed = digitalio.DigitalInOut(board.GP12)
BLed.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print("CODE IS RUNNING")

while True:
    if not button.value:  # Button is pressed (active low)
        RLed.value = not RLed.value
        GLed.value = not GLed.value
        BLed.value = not BLed.value