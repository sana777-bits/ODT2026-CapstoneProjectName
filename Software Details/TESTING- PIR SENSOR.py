# code to test PIR sensor
# wiring: VCC to 5V, OUT to GPIO 4, GND to GND

from machine import Pin
import time

pir = Pin(4, Pin.IN)

print("PIR test running- waiting for motion!!!")

while True:
    if pir.value() == 1:
        print("Success — motion detected!")
        time.sleep(1)   # wait 1s
    time.sleep_ms(100)