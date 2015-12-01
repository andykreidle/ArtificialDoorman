import time
import signal 
import sys
import os, picamera
from Adafruit_ADS1x15 import ADS1x15

#initialize ADC
ads1015 = 0x00 
adc = ADS1x15(ic=ads1015) 

#define camera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

#define picture taking function
def snap_photo(file_name):
	camera.resolution = (1024, 768)	
	camera.capture(file_name)
	print "rpi-ms-camera: Photo taken."

while 1: 
    #read ADC into variable called volts
    volts = adc.readADCSingleEnded(1, 1024, 860)
    print(volts)
    #here is thee knock sensitivity
    if volts > 1024: 
        #take picture and exit
        snap_photo("guest.jpg")
        camera.close()
        sys.exit()
    time.sleep(0.1)
