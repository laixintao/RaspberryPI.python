#!/usr/bin/python2
#coding=utf-8
import RPi.GPIO as GPIO
from config import DISTANCE_IN

GPIO.setmode(GPIO.BCM)
GPIO.setup(DISTANCE_IN,GPIO.IN)

def people_near():
    return GPIO.input(DISTANCE_IN)

if __name__ == "__main__":
    while True:
        if people_near()==True:
            print "T"
        else:
            print "F"
