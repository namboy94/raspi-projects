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

import time

from RPi.GPIO import BCM, OUT, IN, HIGH, LOW, PUD_UP
from RPi.GPIO import setup, setmode, setwarnings, output
from RPi.GPIO import input as _input

BIT_LEDS = [7, 8, 25, 24, 23, 18, 15, 14]
BUTTON = 21
BEEPER = 20
ONE_HUNDRED_LED = 16
TWO_HUNDRED_LED = 12
LSD = [2, 3, 4, 17, 27, 22, 10]
MSD = [9, 11, 5, 6, 13, 19, 26]

def setup_gpio():

    setmode(BCM)
    setwarnings(False)

    for led in BIT_LEDS + [ONE_HUNDRED_LED, TWO_HUNDRED_LED]:
        setup(led, OUT)

    for segment in LSD + MSD:
        setup(segment, OUT)

    setup(BEEPER, OUT)
    setup(BUTTON, IN, pull_up_down=PUD_UP)

    cleanup()

    for segment in [0, 1, 2, 3, 4, 5]:
        output(LSD[segment], HIGH)
        output(MSD[segment], HIGH)


def cleanup():

    for led in BIT_LEDS + [ONE_HUNDRED_LED, TWO_HUNDRED_LED]:
        output(led, LOW)

    for segment in LSD + MSD:
        output(segment, LOW)

    output(BEEPER, LOW)


def draw(number):
    binary = convert_to_8_bit_binary(number)

    for i in range(0, 8):

        if binary[i] == 1:
            output(BIT_LEDS[i], HIGH)
        else:
            output(BIT_LEDS[i], LOW)

    numberstring = str(number).zfill(2)

    draw_lcd(int(numberstring[-1]), LSD)
    draw_lcd(int(numberstring[-2]), MSD)

    if len(numberstring) > 2:

        if numberstring[0] == "1":
            output(ONE_HUNDRED_LED, HIGH)
            output(TWO_HUNDRED_LED, LOW)

        elif numberstring[0] == "2":
            output(ONE_HUNDRED_LED, HIGH)
            output(TWO_HUNDRED_LED, HIGH)

    else:
        output(ONE_HUNDRED_LED, LOW)
        output(TWO_HUNDRED_LED, LOW)


def draw_lcd(digit, lcd):

    active = []
    if digit == 0:
        active = [0, 1, 2, 3, 4, 5]
    elif digit == 1:
        active = [0, 3]
    elif digit == 2:
        active = [1, 2, 3, 4, 6]
    elif digit == 3:
        active = [0, 1, 3, 4, 6]
    elif digit == 4:
        active = [0, 3, 6, 5]
    elif digit == 5:
        active = [0, 1, 4, 5, 6]
    elif digit == 6:
        active = [0, 1, 2, 4, 5, 6]
    elif digit == 7:
        active = [0, 3, 4]
    elif digit == 8:
        active = [0, 1, 2, 3, 4, 5, 6]
    elif digit == 9:
        active = [0, 3, 4, 5, 6]

    for segment in range(0, 7):
        if segment in active:
            output(lcd[segment], HIGH)
        else:
            output(lcd[segment], LOW)


def convert_to_8_bit_binary(number):

    if number > 255:
        return [1, 1, 1, 1, 1, 1, 1, 1]

    binary_numbers = []

    while int(number / 2) >= 1:
        binary_numbers.append(number % 2)
        number = int(number / 2)

    binary_numbers.append(number % 2)

    while len(binary_numbers) < 8:
        binary_numbers.append(0)

    return list(reversed(binary_numbers))

def wait_for_input():
    while _input(BUTTON):
        pass


class Counter(object):

    def __init__(self):
        self.count = 0

    def increment(self):
        if self.count < 255:
            self.count += 1
        draw(self.count)

    def reset(self):
        self.count = 0
        draw(self.count)


if __name__ == "__main__":

    setup_gpio()
    try:
        counter = Counter()
        while True:

            wait_for_input()
            output(BEEPER, HIGH)

            counter.increment()
            time.sleep(0.2)

            output(BEEPER, LOW)

    except KeyboardInterrupt:
        cleanup()
