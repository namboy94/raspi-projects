#!/usr/bin/env python

import time
from RPi.GPIO import BOARD, OUT, IN, HIGH, LOW, setup, setmode, setwarnings

LEFT_TOP = 0
LEFT_MID = 0
LEFT_BOT = 0
RIGHT_TOP = 0
RIGHT_MID = 0
RIGHT_BOT = 0

def setup_gpio():
	setmode(BOARD)
	setwarnings(false)

if __name__ == "__main__":
	setup_gpio()

	setmode(LEFT_TOP, HIGH)

	time.sleep(1)

	setmode(LEFT_TOP, LOW)