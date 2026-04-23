from machine import Pin
import neopixel, time

np = neopixel.NeoPixel(Pin(18), 16)

np.fill((0, 0, 0))
np.write()
time.sleep(1)

for i in range(16):
    np.fill((0, 0, 0))
    np[i] = (0, 0, 255)
    np.write()
    time.sleep(0.3)