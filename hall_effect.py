import RPi.GPIO as GPIO
import sys
import time

#use GPIO pin 13
sensor = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_UP)
while True: 
   #read GPIO
   if GPIO.input(sensor) == 0:
        print("not latched")
	#time until notificatin is sent
        time.sleep(2)
        if GPIO.inptu(sensor) == 0;
            sys.exit()
   if GPIO.input(sensor) == 1:
        print(" latched")
	#time delay, may be reduced for newer modles of rPi
        time.sleep(1)
GPIO.cleanup()
