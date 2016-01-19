#! /usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import time
from config import WAVE_ECHO_IN as ECHO
from config import WAVE_TRIG_OUT as TRIG
import ctypes
import functools
import threading

def _async_raise(tid, exception):
    ret = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exception))
    if ret == 0:
        raise ValueError('Invalid thread id')
    elif ret != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), 0)
        raise SystemError('PyThreadState_SetAsyncExc failed')


class ThreadTimeout(Exception):
    """ Thread Timeout Exception """
    pass


class WorkThread(threading.Thread):
    """ WorkThread """

    def __init__(self, target, args, kwargs):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.start()

    def run(self):
        try:
            self.result = self.target(*self.args, **self.kwargs)
        except Exception as e:
            self.exception = e
        else:
            self.exception = None

    def get_tid(self):
        if self.ident is None:
            raise threading.ThreadError('The thread is not active')
        return self.ident

    def raise_exc(self, exception):
        _async_raise(self.get_tid(), exception)

    def terminate(self):
        self.raise_exc(SystemExit)


def timeout(timeout):
    """ timeout decorator """
    def proxy(method):
        @functools.wraps(method)
        def func(*args, **kwargs):
            worker = WorkThread(method, args, kwargs)
            worker.join(timeout=timeout)
            if worker.is_alive():
                worker.terminate()
                raise ThreadTimeout('A call to %s() has timed out' % method.__name__)
            elif worker.exception is not None:
                raise worker.exception
            else:
                return worker.result
        return func
    return proxy

@timeout(2)
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
    dis = (t2-t1)*340/2
    #for test
    print dis
    return dis

def no_people_near():
    try:
        dis = checkdist()
        if dis > 0.5:
            return True
        else:
            return False
    except ThreadTimeout as e:
        return True
    return True



GPIO.setmode(GPIO.BCM)
#第15号针，GPIO22
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
#第16号针，GPIO23
GPIO.setup(ECHO,GPIO.IN)

time.sleep(2)

if __name__ == "__main__":
    while True:
        print "is there people?",
        print no_people_near()