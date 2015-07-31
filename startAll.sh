#!/bin/sh

python2.7 TCPserver3.py &
echo $! >> pid.log
sleep 1
python2.7 serialTest3.py &
echo $! >> pid.log
