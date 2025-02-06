"""
Blink Program
Blink led on pin 2 for 1 second period
"""
import time
from machine import Pin

led=Pin(2,Pin.OUT)
 
while True:
    led.value(1) #or led.on()
    time.sleep(1)
    led.value(0) # or led.off()
    time.sleep(1)
