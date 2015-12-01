import RPi.GPIO as GPIO
import time
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

sensor = 27
waitTime = 1
while True:
    if GPIO.input(sensor) == 0:
        print('unlatched')
        time.sleep(waitTime)
        if GPIO.input(sensor) == 0:
            os.system("""./unlatchNotification.sh""")
    else:
        print('latched')
GPIO.cleanup()
