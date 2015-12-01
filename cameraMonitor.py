import RPi.GPIO as GPIO
import os, picamera, sys, time
import subprocess

GPIO.setmode(GPIO.BCM)
#plug passive infrared into GPIO pin 19
PIR_PIN = 19
GPIO.setup(PIR_PIN, GPIO.IN)

#initialize camera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

#can be used for time stamps but pictures will be saved to email
def generate_file_name():
	return time.strftime("%Y-%m-%d-%H-%M-%S-%Z", time.localtime())
    
def snap_photo(file_name):
	camera.resolution = (1024, 768)	
	camera.capture(file_name)
	print "rpi-ms-camera: Photo taken."
	

#wait for rising edge of GPIO
GPIO.wait_for_edge(PIR_PIN, GPIO.RISING)
print ("Motion Detected!")
#fname = LOCAL_DIRECTORY + generate_file_name()
#fname = fname + ".jpg"
snap_photo(guest.jpg)
camera.close()
GPIO.cleanup()
sys.exit()
