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

TOP_ROW = [25, 24, 23, 18, 15, 14]
MIDDLE_ROW = [8, 7, 12, 16, 20, 21]
BOTTOM_ROW = [5, 22, 27, 17, 4, 3, 2]

TOP_ADD_BUTTON = 26
TOP_SUB_BUTTON = 13
BOT_ADD_BUTTON = 19
BOT_SUB_BUTTON = 6


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


def draw_number(number, row):

    binary = convert_to_binary(number)

    while len(binary) < len(row):
        binary = [0] + binary

    for i in range(0, len(row)):

        if binary[i] == 1:
            output(row[i], HIGH)
        else:
            output(row[i], LOW)


def convert_to_binary(number):

    binary_numbers = []

    while int(number / 2) >= 1:
        binary_numbers.append(number % 2)
        number = int(number / 2)

    binary_numbers.append(number % 2)

    return list(reversed(binary_numbers))


def wait_for_input():

    while True:

        if not _input(TOP_ADD_BUTTON):
            return "TOP_ADD"
        elif not _input(TOP_SUB_BUTTON):
            return "TOP_SUB"
        elif not _input(BOT_ADD_BUTTON):
            return "MID_ADD"
        elif not _input(BOT_SUB_BUTTON):
            return "MID_SUB"
        else:
            pass


def increment(number):
    if number < 63:
        return number + 1
    else:
        return number


def decrement(number):
    if number > 0:
        return number - 1
    else:
        return number


class Adder(object):

    def __init__(self):

        self.TOP_VALUE = 0
        self.MID_VALUE = 0

    def process_command(self, command):

        if command == "TOP_ADD":
            self.TOP_VALUE = increment(self.TOP_VALUE)
        elif command == "TOP_SUB":
            self.TOP_VALUE = decrement(self.TOP_VALUE)
        elif command == "MID_ADD":
            self.MID_VALUE = increment(self.MID_VALUE)
        elif command == "MID_SUB":
            self.MID_VALUE = decrement(self.MID_VALUE)

    def refresh(self):

        draw_number(self.TOP_VALUE, TOP_ROW)
        draw_number(self.MID_VALUE, MIDDLE_ROW)
        draw_number(self.TOP_VALUE + self.MID_VALUE, BOTTOM_ROW)


if __name__ == "__main__":

    setup_gpio()
    adder = Adder()
    try:

        while True:
            command = wait_for_input()
            adder.process_command(command)
            adder.refresh()
            time.sleep(0.2)

    except KeyboardInterrupt:
        cleanup()
