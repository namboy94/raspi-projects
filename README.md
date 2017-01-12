# Raspberry Pi 8-bit Counter

A Raspberry Pi Project that counts an 8-bit number and displays it in
a human-readable format.

## Setup

The Layout looks like this:

![The Layout of the Raspberry Pi 8-bit counter](layout.jpg)

The Red LEDs, which are used to display the current number in binary,
are connected to the GPIO pins 7, 8, 25, 24, 23, 18, 15 and 14.

The Most Siginificant Digit LCD is connected to the Pins
9, 11, 5, 6, 13, 19 and 26, whereas the Least Significant Digit LCD is
connected to the Pins 2, 3, 4, 17, 27, 22 and 10.

The button is connected to Pin 21, the beeper to pin 20.

Two LEDs to indicate a number of 100 and 200 are connected to
pins 16 and 12 respectively.

## Demonstration

A demonstration video is available on
[Youtube](https://youtu.be/8YgGTAfsWaA)

## Usage

The program itself is used by running ```python 8-bit-counter.py```

## Links

* [Github](https://github.com/namboy94/raspi-8-bit-counter)
* [Gitlab](https://gitlab.namibsun.net/namboy94/raspi-8-bit-counter)