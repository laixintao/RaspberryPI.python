#!/usr/bin/python
import RPi.GPIO as GPIO
import time

n = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(n,GPIO.OUT)

while True:
	GPIO.output(n,True)
	print "HIGH..."
	time.sleep(1)
	print "LOW..."
	GPIO.output(n,False)
	time.sleep(1)
