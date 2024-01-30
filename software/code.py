import board
import digitalio
import time


# LED and Button Configuration
# ----------------------------

# Initialize digital outputs for each LED
led_gpio_pins = [board.GP12, board.GP13, board.GP14]
leds = [digitalio.DigitalInOut(pin) for pin in led_gpio_pins]
for led in leds:
    led.direction = digitalio.Direction.OUTPUT

# Initialize the button with pull-up resistor
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

print("CODE IS RUNNING")


# Function to Change LED States
# -----------------------------

# Each tuple represents the state (1 = ON, 0 = OFF) of Red, Green, and Blue LEDs
led_states = [
    (0, 0, 0),  # All LEDs off
    (1, 0, 1),  # Red and Blue LEDs on
    (1, 1, 1)   # All LEDs on
]

def change_led_state(state_index):
    """
    Update the state of each LED based on the specified index.
    :param state_index: Index to select the LED state from led_states.
    """
    for led, state in zip(leds, led_states[state_index]):
        led.value = state


# Main Program Loop
# -----------------

state_index = 0  # Index to track the current LED state

while True:
    if not button.value: # button is pressed
        # Cycle through the LED states
        state_index = (state_index + 1) % len(led_states)
        change_led_state(state_index)

        # Delay to prevent button bounce issues
        time.sleep(0.2)

