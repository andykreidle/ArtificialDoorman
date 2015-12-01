import RPi.GPIO as GPIO
import time

#make sure the pin numbers are given by broadcom
GPIO.setmode(GPIO.BCM)

#pin numbers and variables
Motor1A = 21  #input 1
Motor1B = 16  #input 2
Motor1E = 20  #enable pin

#set duty cycle,  input, and output pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
pwm1A = GPIO.PWM(Motor1A, 250)
GPIO.setup(Motor1B,GPIO.OUT)
pwm1B = GPIO.PWM(Motor1B, 250)

#initialize pulse width modulation
pwm1A.start(1)
pwm1B.start(1)

#start locking and unlocking
print "Unlocking......"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

pwm1A.ChangeDutyCycle(50)

time.sleep(0.2)
GPIO.output(Motor1E,GPIO.LOW)
time.sleep(3)
GPIO.output(Motor1E,GPIO.HIGH)

print "...Locking..."
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
pwm1B.ChangeDutyCycle(100)
time.sleep(0.2)
 
print "Tada!"
GPIO.output(Motor1E,GPIO.LOW)


pwm1A.stop()
pwm1B.stop()
GPIO.cleanup()
