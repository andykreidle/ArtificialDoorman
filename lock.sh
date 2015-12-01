#!/bin/bash

while true
do
#remove old inbox file
sudo rm inbox.txt
#read inbox into text file
timeout --foreground 20 mutt >> inbox.txt
#search inbox file for Unlock command
grep Unlock inbox.txt
if [ $? -eq 0 ];
then
        #trigger unlock.. 2sec.. lock program
	sudo python h-bridge_locking.py
        #move inbox to gmail trash
	sudo python del.py
fi
echo "....done...."
done
