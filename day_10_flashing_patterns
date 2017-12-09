# Day 10 - Christmas tree flashing patterns

# Requirements
1. A two part wooden tree
2. Breadboard
3. Resistors (two or three depending on how many groups you want)
4. LEDs (up to five)
5. Male to female wires 
6. Raspberry Pi Zero, screen, keyboard, mouse and adaptors to make it all work


# Summary of Steps
1. Create two separate circuits with a resistor and half of the LEDs in parallel
2. Connect each circuit input to separate pins in Pi Zero - from GPIO 21 to your first circuit on breadboard 
3. From GPIO 20 to the second circuit on breadboard.... 
4. Connect both circuits to negative (-) on the breadboard and from the breadboard to GND on the Pi Zero
5. Check [Pi GPIO Schematic](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2) to be sure of numbers 
6. Open Python 3 IDE
7. Open a new file and save it with a name... e.g. xmas_light2.py (you could adapt yesterdays...)
8. Here is a simple script
``` python
from gpiozero import LED
from time import sleep

leds_1 = LED(21)
leds_2 = LED(20)

while True:
  leds_1.on()
  led_2.off()
  sleep(1)
  leds_1.on()
  led_2.on()
  sleep(1)
  leds_1.off()
  led_2.on()
  sleep(1)
  leds_1.off()
  led_2.off()
  sleep(1) 
  
```
9. Save the file 
10. Run the file using Run module. 
11. Experiment - how many different patterns can you make?
12. Experiment - do you fancy adding a third group?


[Inspiration and Hat Tip to Cat Lamin](https://catlamin.com/2017/04/16/an-easter-gift-rpi-beginners-worksheet/)

[Picture Link](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/images/gpio-numbers-pi2.png)

