# -*- coding: utf-8 -*-
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

TRIG = 20
ECHO = 17

RPi.GPIO.setup(TRIG, RPi.GPIO.OUT)
RPi.GPIO.setup(ECHO, RPi.GPIO.IN)

try:
    while True:
        RPi.GPIO.output(TRIG, 0)
        time.sleep(0.01)

        RPi.GPIO.output(TRIG, 1)
        time.sleep(0.01)
        RPi.GPIO.output(TRIG, 0)
        start = time.time()
        stop = time.time()

        while RPi.GPIO.input(ECHO) == 0:
            start = time.time()

        while RPi.GPIO.input(ECHO) == 1:
            stop = time.time()

        distance = (stop - start - 0.01) * 34000 / 2 #声波的速度是340m/s
        print distance
except KeyboardInterrupt:
    RPi.GPIO.cleanup()