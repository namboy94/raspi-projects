#!/usr/bin/env python

import time
from RPi.GPIO import BCM, OUT, IN, HIGH, LOW
from RPi.GPIO import setup, setmode, setwarnings, output

LEFT_TOP = 17
LEFT_MID = 0
LEFT_BOT = 0
RIGHT_TOP = 0
RIGHT_MID = 0
RIGHT_BOT = 0

def setup_gpio():
	setmode(BCM)
	setwarnings(False)

	setup(LEFT_TOP, OUT)

if __name__ == "__main__":
	setup_gpio()

	output(LEFT_TOP, HIGH)

	time.sleep(1)

	output(LEFT_TOP, LOW)