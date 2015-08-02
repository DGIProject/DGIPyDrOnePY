#!/bin/sh

gpio mode 0 in

isPressed=false
countPressed=0

firstTime=true

while true; do
 value=$(gpio read 0)

 echo $countPressed

 if [ $value = 1 ]
 then
  isPressed=true
  countPressed=$((countPressed+1))

  firstTime=true
 else
  isPressed=false
 fi

 if [ $isPressed = false ] && [ $firstTime = true ]
 then
  if [ $countPressed -gt 200 ]
  then
   echo "reboot"
   #reboot
  elif [ $countPressed -gt 100 ]
  then
   echo "halt"
   #halt
  else
   echo "--ACTION--"
   echo "stop scripts"
   ./killAll.sh
   sleep 30
   echo "start scripts"
   ./startAll.sh
  fi

  firstTime=false
  countPressed=0
 fi
done
