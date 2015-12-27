
import os

def screen_on():
    os.system("xset dpms force on")

def screen_off():
    os.system("xset dpms force off")

if __name__=="__main__":
    import time
    screen_off()
    time.sleep(2)
    screen_on()