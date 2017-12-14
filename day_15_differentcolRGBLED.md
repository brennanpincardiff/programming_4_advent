# Day 15 - Make our RGB LED go different colours

# Steps
1. Wire up each RGB LED to a separate resistor
2. Start up your Raspberry Pi


``` python
from gpiozero import RGBLED
from time import sleep

led = RGBLED(16,20,21)

mode1 = (1,0,0)
mode2 = (0,1,0)

while True:
    led.color = (1,0,0)
    sleep(1)
    led.color = (0,0,1)
    sleep(1)
    led.color = (0,1,0)
    sleep(1)
    led.color = (1,1,0)
    sleep(1)
    led.color = (0,1,1)
    sleep(1)
    led.color = (0.25,0,1)
    sleep(1)
``` 
On Pi as rgbled1.py
