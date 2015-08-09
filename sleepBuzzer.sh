#!/bin/sh

gpio mode 27 out
gpio mode 28 out

countBuzzer=0
finish=true

while $finish
do
 gpio write 27 1
 gpio write 28 1

 sleep 0.5

 gpio write 27 0
 gpio write 28 0

 sleep 0.5

 countBuzzer=$(($countBuzzer + 1))

 if [ $countBuzzer -ge $1 ]
 then
  finish=false
 fi
done

gpio write 27 0
gpio write 28 0

