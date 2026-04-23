from machine import Pin
import time

p = Pin(18, Pin.OUT)

while True:
    p.value(1)
    time.sleep(2)
    p.value(0)
    time.sleep(2)