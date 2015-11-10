
from send import send_email
from shoot import shoot

if __name__ == "__main__":
    filename = shoot()
    send_email("Photo","Picture From RaspberryPI.",filename)