from machine import Pin
import time

# pins
motor_pins = [
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT),
    Pin(22, Pin.OUT),
    Pin(21, Pin.OUT)
]

# sequence test
STEP_SEQUENCE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

step_index = 0

def step_motor(steps, delay=3):
    global step_index

    direction = 1 if steps > 0 else -1
    steps = abs(steps)

    for _ in range(steps):
        pattern = STEP_SEQUENCE[step_index]

        for i in range(4):
            motor_pins[i].value(pattern[i])

        step_index = (step_index + direction) % 8
        time.sleep_ms(delay)

def stop_motor():
    for pin in motor_pins:
        pin.value(0)

# 512 ≈ 90°
STEPS_90 = 1023

while True:
    print("90 degrees forward")
    step_motor(STEPS_90)
    stop_motor()
    time.sleep(2)

    print("90 degrees backward")
    step_motor(-STEPS_90)
    stop_motor()
    time.sleep(2)