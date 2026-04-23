from machine import Pin
import neopixel, time

np = neopixel.NeoPixel(Pin(27), 16)

for j in range(8):
    np[j] = (0, 255, 0)
np.write()
time.sleep(3.3)

for j in range(8):
    np[j] = (255, 165, 0)
np.write()
time.sleep(3.3)

for j in range(8):
    np[j] = (255, 0, 0)
np.write()
time.sleep(3.4)