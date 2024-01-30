# LED and Button Control

## Setup
- LEDs: Initialize on GPIO pins GP12, GP13, GP14 as OUTPUT.
- Button: Initialize on GPIO pin GP15 as INPUT with pull-up.

## LED States
- Define states: OFF, Red+Blue ON, All ON.

## Function: Change LED State
- Update LEDs based on a given state index.

## Main Loop
- Monitor button press.
- Cycle through LED states on press.
- Include debounce delay.
