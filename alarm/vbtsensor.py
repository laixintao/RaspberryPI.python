#!/usr/bin/env python

__author__ = 'laixintao'

 # +-----+-----+---------+------+---+---Pi 2---+---+------+---------+-----+-----+
 # | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 # +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 # |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 # |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5V      |     |     |
 # |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 # |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT0 | TxD     | 15  | 14  |
 # |     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |
 # |  17 |   0 | GPIO. 0 |  OUT | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 # |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 # |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 # |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 # |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 # |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 # |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 # |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 # |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 # |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 # |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 # |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 # |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 # |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 # |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 # +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 # | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 # +-----+-----+---------+------+---+---Pi 2---+---+------+---------+-----+-----+

import RPi.GPIO
import time

from config import VBTSENSOR_IN

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(VBTSENSOR_IN,RPi.GPIO.IN)

def get_status():
    return RPi.GPIO.input(VBTSENSOR_IN)

if __name__ == "__main__":
    while True:
        if get_status() == 1:
            pass
        else:
            print "0"