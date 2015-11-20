
from send import send_email
from shoot import shoot
from buzzer import ring,alarm
from vbtsensor import get_status
import threading
import time

class thread_ring(threading.Thread):
    def run(self):
        # print "start ring..."
        ring()
        # print "ring over..."

class thread_shoot(threading.Thread):
    def run(self):
        print "strat pic..."
        self.shoot_pictures()
        print "pic over..."
    def shoot_pictures(self):
        filename = shoot()
        send_email("Photo","Picture From RaspberryPI.",filename)

def alert():
    while True:
        if get_status()==0 :
            tr = thread_ring()
            # ts = thread_shoot()
            tr.start()
            # ts.start()

if __name__ == "__main__":
    alert()