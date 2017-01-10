#!/usr/bin/env python

import time
from RPi.GPIO import BCM, OUT, IN, HIGH, LOW
from RPi.GPIO import setup, setmode, setwarnings, output

LEFT_TOP = 22
LEFT_MID = 27
LEFT_BOT = 17
RIGHT_TOP = 2
RIGHT_MID = 3
RIGHT_BOT = 4
BUTTON = 14

def setup_gpio():
	setmode(BCM)
	setwarnings(False)

	setup(LEFT_TOP, OUT)
	setup(LEFT_MID, OUT)
	setup(LEFT_BOT, OUT)
	setup(RIGHT_TOP, OUT)
	setup(RIGHT_MID, OUT)
	setup(RIGHT_BOT, OUT)
	setup(BUTTON, IN)

if __name__ == "__main__":
	setup_gpio()

	for i in [22,27,17,2,3,4]:

		output(i, HIGH)

		time.sleep(1)

		output(i, LOW)