# Day 9 - Let's make our Christmas Tree flash

# Requirements
1. A two part wooden tree
2. Breadboard
3. Resistor
4. LEDs (up to five)
5. Male to female wires 
6. Raspberry Pi Zero, screen, keyboard, mouse and adaptors to make it all work


# Summary of Steps
1. Use circuit from yesterday - I recommend that you connect the LED in parallel
2. Parallel connection - resistor from + to one of the rows above; long LED ends to resistor rail; short LED ends to negative rail (-)
3. But instead of battery, connect to Pi Zero - from GPIO 21 to positive on breadboard (+); from GND to negative on breadboard
4. Check [Pi GPIO Schematic](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2) to be sure of numbers 
5. Open Python 3 IDE
6. Open a new file and save it with a name... e.g. xmas_light.py
7. Here is a simple script
``` python
from gpiozero import LED
from time import sleep

leds_on = LED(21)

while True:
  leds_on.on()
  sleep(1)
  leds_on.off()
  sleep(1)
```
8. Save the file 
9. Run the file using Run module. 


[Inspiration and Hat Tip to Cat Lamin](https://catlamin.com/2017/04/16/an-easter-gift-rpi-beginners-worksheet/)

[Picture Link](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/images/gpio-numbers-pi2.png)


