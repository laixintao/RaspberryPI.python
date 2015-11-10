__author__ = 'laixintao'

import os
import time

def shoot(quality=100,width=1000,height=1000):
    print "now time:",
    pic_name = str(time.time())+".jpeg"
    print pic_name[:-5]
    print "shoot picture..."
    os.system("raspistill -o /tmp/"
              +str(pic_name)
              +" -q "+str(quality)
              +" -h "+str(height)
              +" -w "+str(width))
    print "picture ok..."
    abs_path = '/tmp/'+str(pic_name)
    return abs_path