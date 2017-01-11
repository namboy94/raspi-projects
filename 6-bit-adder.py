#!/usr/bin/env python
"""
Copyright Hermann Krumrey <hermann@krumreyh.com>, 2017

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from RPi.GPIO import BCM, OUT, IN, HIGH, LOW, PUD_UP
from RPi.GPIO import setup, setmode, setwarnings, output
from RPi.GPIO import input as _input

TOP_ROW = [14, 15, 18, 23, 24, 25]
MIDDLE_ROW = [8, 7, 12, 16, 20. 21]
BOTTOM_ROW = [2, 3, 4, 17, 27, 22]

TOP_ADD_BUTTON = 6
TOP_SUB_BUTTON = 13
BOT_ADD_BUTTON = 19
BOT_SUB_BUTTON = 26


def setup_gpio():
    setmode(BCM)
    setwarnings(False)

    for led in TOP_ROW + MIDDLE_ROW + BOTTOM_ROW:
        setup(led, OUT)

    setup(TOP_ADD_BUTTON, IN, pull_up_down=PUD_UP)
    setup(TOP_SUB_BUTTON, IN, pull_up_down=PUD_UP)
    setup(BOT_ADD_BUTTON, IN, pull_up_down=PUD_UP)
    setup(BOT_SUB_BUTTON, IN, pull_up_down=PUD_UP)
    cleanup()


def cleanup():
    for led in TOP_ROW + MIDDLE_ROW + BOTTOM_ROW:
        output(led, LOW)


if __name__ == "__main__":

	setup_gpio()

	for led in TOP_ROW + MIDDLE_ROW + BOTTOM_ROW:
        output(led, HIGH)
        time.sleep(1)

    cleanup()