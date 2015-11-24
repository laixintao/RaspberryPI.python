import RPi.GPIO as GPIO
import time

IN = 27

GPIO.setup(IN,GPIO.IN)

def is_there_human():
    return GPIO.input(IN)

if __name__=='__main__':
    try:
        while True:
            print is_there_human()
    except KeyboardInterrupt:
        RPi.GPIO.cleanup()