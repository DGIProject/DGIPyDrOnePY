#!/bin/sh

gpio mode 0 in

isPressed=false
firstTime=true

while true; do
 value=$(gpio read 0)

 #echo $isPressed

 if [ $value = 1 ]
 then
  isPressed=true
  firstTime=true
 else
  isPressed=false
 fi

 if [ $isPressed = false ] && [ $firstTime = true ]
 then
  firstTime=false
  echo "--ACTION--"
  echo "stop scripts"
  ./killAll.sh
  sleep 5
  echo "start scripts"
  ./startAll.sh
 fi
done
