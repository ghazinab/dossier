import board
import digitalio
import time

def Switch(i):
    if i == 0:
        RLed.value = 0
        GLed.value = 0
        BLed.value = 0
    elif i == 1:
        RLed.value = 1
        GLed.value = 0
        BLed.value = 1
    elif i == 2:
        RLed.value = 1
        GLed.value = 1
        BLed.value = 0

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

i = 0

while True:
    i += 1 if button.value else 0  # Increment i only if button is pressed
    time.sleep(0.1)
    i = 0 if i > 2 else i  # Reset i to 0 if it exceeds 2
    Switch(i)
