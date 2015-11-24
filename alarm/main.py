
from send import send_email
from shoot import shoot
from buzzer import ring,alarm
from vbtsensor import get_status

def alert():
    while True:
        if get_status()==0 :
            ring()

if __name__ == "__main__":
    alert()