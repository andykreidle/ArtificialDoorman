#!/bin/bash
import os, sys, time, datetime, picamera
import RPi.GPIO as GPIO

def PIR_detection(sensor):
    if (GPIO.input(sensor) == True):
        return True
    else:
        return False
    
def main():
    pir_sensor = 17
    # gpio pin on rpi set to input
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_sensor, GPIO.IN)
    while True:
        time.sleep(0.1)
        if PIR_detection(pir_sensor) == False:
            print("snap")
            #os.system("""raspistill -o /home/pi/doorman/picture.jpg""")
            #os.system("""sudo mutt -s \"test\" PHONENUMBER@txt.att.net < nada.txt""")
            #os.system("""./arrivalNote.sh""")
            time.sleep(1)

            
main()
