import RPi.GPIO as GPIO
import time
from buzzer import ring,buzzer_end,buzzer_start

IN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN,GPIO.IN)

def is_there_human():
    return GPIO.input(IN)

if __name__=='__main__':
    try:
        while True:
            if is_there_human()==1:
                buzzer_start()
                # print time.time(),": ","True"
            else:
                buzzer_end()
                print time.time(),"--"
    except KeyboardInterrupt:
        GPIO.cleanup()
        buzzer_end()