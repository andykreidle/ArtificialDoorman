#!/bin/bash

while true
do
#read the ADC/piezo until it hits the threshold
sudo python piezo.py
#or run the passive infrared sensor(motion sensor)
#sudo python monitor_camera.py
#send a notification
mutt -s "    Someone has arrived" PHONENUMBER@txt.att.net < arrival.txt
#send the picture
mutt -s " guest picture " YOURemail@gmail.com -a guest.jpg < nada.txt
done
