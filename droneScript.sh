#!/bin/sh

gpio mode 0 in

gpio mode 27 out
gpio mode 28 out

isPressed=false
firstTimePressed=false

countBuzzer=0
isBuzzing=false

timeStart=$(cat /proc/uptime | cut -d'.' -f1)
timeEnd=0

firstTime=true

while true; do
 value=$(gpio read 0)

 if [ $isPressed = false ] && [ $firstTime = true ]
 then
  timeEnd=$(cat /proc/uptime | cut -d'.' -f1)

  gapTime=$(($timeEnd - $timeStart))

  if [ $gapTime -ge 10 ]
  then
   echo "--DRONESCRIPT-- reboot server"
   #reboot
  elif [ $gapTime -ge 5 ]
  then
   echo "--DRONE SCRIPT-- halt server"
   #halt
  else
   echo "--DRONE SCRIPT-- stop scripts, wait 120 seconds"
   #./killAll.sh
   ./sleepBuzzer.sh 5

   echo "--DRONE SCRIPT-- start scripts"
   #./startAll.sh
  fi

  firstTime=false
 fi

 if [ $value = 1 ]
 then
  isPressed=true

  if [ $firstTimePressed = false ]
  then
   timeStart=$(cat /proc/uptime | cut -d'.' -f1)

   firstTimePressed=true
  fi

  timeEnd=$(cat /proc/uptime | cut -d'.' -f1)

  gapTime=$(($timeEnd - $timeStart))

  if [ $gapTime -ge 10 ]
  then
   if [ $countBuzzer -ge 2 ]
   then
    countBuzzer=0
    isBuzzing=$([ $isBuzzing = false ] && echo true || echo false)
   fi

   countBuzzer=$(($countBuzzer + 1))

   if [ $isBuzzing = true ]
   then
    gpio write 27 1
    gpio write 28 1
   else
    gpio write 27 0
    gpio write 28 0
   fi
  elif [ $gapTime -ge 5 ]
  then
   if [ $countBuzzer -ge 5 ]
   then
    countBuzzer=0
    isBuzzing=$([ $isBuzzing = false ] && echo true || echo false)
   fi

   countBuzzer=$(($countBuzzer + 1))

   if [ $isBuzzing = true ]
   then
    gpio write 27 1
    gpio write 28 1
   else
    gpio write 27 0
    gpio write 28 0
   fi
  else
   if [ $countBuzzer -ge 15 ]
   then
    countBuzzer=0
    isBuzzing=$([ $isBuzzing = false ] && echo true || echo false)
   fi

   countBuzzer=$(($countBuzzer + 1))

   if [ $isBuzzing = true ]
   then
    gpio write 27 1
    gpio write 28 1
   else
    gpio write 27 0
    gpio write 28 0
   fi
  fi


  firstTime=true
 else
  isPressed=false
  firstTimePressed=false

  if [ $countBuzzer -lt 10 ]
  then
   gpio write 27 1
   gpio write 28 1
  else
   gpio write 27 0
   gpio write 28 0

   if [ $countBuzzer -gt 100 ]
   then
    countBuzzer=0
   fi
  fi

  countBuzzer=$(($countBuzzer + 1))
 fi
done
