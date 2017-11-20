# Raspberry Pi 6-bit Addition Calculator

This Raspberry Pi Project consists of 3 rows of LEDs and 4 buttons.
The rows of LEDs show binary numbers (2 6-bit numbers and one 7-bit).
The buttons are used to add and subtract from the two 6-bit numbers.
The 7-bit number is always the sum of the two 6-bit numbers.

## Setup

The Layout looks like this:

![The Layout of the Raspberry Pi 6-bit Adder](layout.jpg)

The Upper LED row is connected to the Pins 14, 15, 18, 23, 24, 25.

The Middle LED row is connected to the Pins 7, 8, 12, 16, 20, 21.

The Lower LED row is connected to the Pins 2, 3, 4, 5, 17, 22, 27.

The buttons are connected to Pins 6, 13, 19, 26.

## Demonstration

A demonstration video is available on
[Youtube](https://www.youtube.com/watch?v=Izo1Rabzk5Q)

## Usage

The program itself is used by running ```python 6-bit-adder.py```
