#!/bin/sh

python2.7 TCPserver4.py &
echo $! >> pid.log

./shellArduino.sh &
echo $! >> pid.log
