# Day 16 - Use a button to make RGB LED go different colours

# Steps
1. Wire up each RGB LED to a separate resistor
2. Start up your Raspberry Pi
3. Wire in a button - ideally to GPIO 11, you need a ground too and probably a resistor



``` python
from gpiozero import RGBLED, Button
from time import sleep

led = RGBLED(16,20,21)
button = Button(11)

mode1 = (1,0,0)
mode2 = (0,1,0)

while True:
    led.color = (1,0,0)
    button.wait_for_press()
    button.wait_for_release()
    
    led.color = (0.25,0,1)

    button.wait_for_press()
    button.wait_for_release()

    led.color = (0.1,0,1)

    button.wait_for_press()
    button.wait_for_release()

    led.color = (0,0,1)

    button.wait_for_press()
    button.wait_for_release()

    led.color = (0,1,0)
    button.wait_for_press()
    button.wait_for_release()

    led.color = (0.1,1,0)
    button.wait_for_press()
    button.wait_for_release()

    led.color = (0.25,1,0)
    button.wait_for_press()
    button.wait_for_release()
``` 
On Pi as rainbow_button.py

Inspiration: MagPi Make a Christmas Star(https://github.com/themagpimag/magpi-issue64/blob/master/XmasStar/star_lights.py)
