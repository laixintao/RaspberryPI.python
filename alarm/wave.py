#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time
from config import WAVE_ECHO_IN as ECHO
from config import WAVE_TRIG_OUT as TRIG

def checkdist():
    #发出触发信号
    GPIO.output(TRIG,GPIO.HIGH)
    #保持10us以上（我选择15us）
    time.sleep(0.000015)
    GPIO.output(TRIG,GPIO.LOW)
    while not GPIO.input(ECHO):
        pass
    #发现高电平时开时计时
    t1 = time.time()
    while GPIO.input(ECHO):
        pass
    #高电平结束停止计时
    t2 = time.time()
    #返回距离，单位为米
    return (t2-t1)*340/2

GPIO.setmode(GPIO.BCM)
#第15号针，GPIO22
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
#第16号针，GPIO23
GPIO.setup(ECHO,GPIO.IN)

time.sleep(2)

try:
    while True:
        print 'Distance: %0.2f m' %checkdist()
    time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()