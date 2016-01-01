#!/bin/sh

./shellArduino.sh > logs/shellArduino.log &
echo $! >> pid.log

sleep 30

rm ip.info
echo `ifconfig wlan0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'` > ip.info

/usr/bin/python2.7 TCPserver.py > logs/TCPserver.log &
echo $! >> pid.log

