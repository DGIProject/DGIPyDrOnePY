#!/bin/bash

stty -F /dev/ttyACM0 cs8 115200 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts

#tail -f /dev/ttyACM0

cat /dev/ttyACM0 > output.txt &
echo $! >> pid.log

while true
do
 #echo -n $(tail -2 output.txt | head -1) > /dev/tcp/192.168.95.27/5005
 echo -n $(tail -2 output.txt | head -1) > lastProperties.txt

 sleep 0.3
done
