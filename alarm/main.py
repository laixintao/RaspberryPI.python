
from send import send_email
from shoot import shoot
from buzzer import ring,alarm
from vbtsensor import get_status
import threading
from wave import no_people_near
from CMD import screen_on,screen_off
import time

class Open(threading.Thread):
    def run(self):
        while True:
            people = no_people_near()
            if not people:
                print "screen on"
                screen_on()

class Close(threading.Thread):
    def run(self):
        _time = 0
        while True:
            print _time
            if not no_people_near():
                _time=0
            else:
                _time+=1
            if _time >= 3:
                _time=0
                screen_off()
                print "screen off"
                # time.sleep(0.1)

class Screen(threading.Thread):
    def run(self):
        _time = 0
        while True:
            print _time
            if not no_people_near():
                _time=0
                screen_on()
            else:
                _time+=1
            if _time >= 3:
                _time=0
                screen_off()
                print "screen off"
                # time.sleep(0.1)


class Alart(threading.Thread):
    def run(self):
        while True:
            if get_status()==0 :
                ring()

if __name__ == "__main__":
    # print "alart..."
    # thread.start_new_thread(alert,())
    # print "open..."
    # thread.start_new_thread(open,())
    # thread.start_new_thread(close,())
    # Open().start()


    # Screen().start()
    # Alart().start()
    _time = 0
    while True:
        print _time
        if not no_people_near():
            _time=0
            screen_on()
        else:
            _time+=1
        if _time >= 90:
            _time=0
            screen_off()
            print "screen off"
            # time.sleep(0.1)