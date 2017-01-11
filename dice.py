#!/usr/bin/env python

import time
import random
from RPi.GPIO import BCM, OUT, IN, HIGH, LOW, PUD_UP
from RPi.GPIO import setup, setmode, setwarnings, output
from RPi.GPIO import input as _input

LEDS = [22, 27, 17, 2, 3, 4]
BUTTON = 14

def setup_gpio():
    setmode(BCM)
    setwarnings(False)

    for led in LEDS:
        setup(led, OUT)

    setup(BUTTON, IN, pull_up_down=PUD_UP)
    cleanup()

def cleanup():
    for led in LEDS:
        output(led, LOW)

def wait_for_button_press():
    while _input(BUTTON):
        pass

def randomize(led):

    if random.randint(0, 1) == 1:
        output(led, HIGH)
    else:
        output(led, LOW)

if __name__ == "__main__":

    try:
        setup_gpio()

        while True:

            wait_for_button_press()

            end_time = time.time() + 3

            while time.time() < end_time:
                for led in LEDS:
                    randomize(led)
                time.sleep(0.2)
    except KeyboardInterrupt:

        cleanup()

