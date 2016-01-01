#!/bin/sh

/usr/local/bin/gpio mode 0 in

/usr/local/bin/gpio mode 27 out
/usr/local/bin/gpio mode 28 out

isPressed=false
firstTimePressed=false

countBuzzer=0
isBuzzing=false

timeStart=$(cat /proc/uptime | cut -d'.' -f1)
timeEnd=0

firstTimeStart=true
firstTime=true

cd /root/DGIPyDrOnePY/

rm ip.info
echo `ifconfig wlan0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'` > ip.info

while true; do
 value=$(/usr/local/bin/gpio read 0)

 if [ $isPressed = false ] && [ $firstTime = true ]
 then
  timeEnd=$(cat /proc/uptime | cut -d'.' -f1)

  gapTime=$(($timeEnd - $timeStart))

  if [ $gapTime -ge 10 ]
  then
   echo "--DRONESCRIPT-- reboot server"
   reboot
  elif [ $gapTime -ge 5 ]
  then
   echo "--DRONE SCRIPT-- halt server"
   halt
  else
   if [ $firstTimeStart = true ]
   then
    echo "--DRONE SCRIPT-- first time"

    firstTimeStart=false
   else
    echo "--DRONE SCRIPT-- stop scripts, wait 120 seconds"
    ./killAll.sh > logs/killAll.log
    ./sleepBuzzer.sh 120
   fi

   echo "--DRONE SCRIPT-- start scripts"
   ./startScriptsDrone.sh
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
    /usr/local/bin/gpio write 27 1
    /usr/local/bin/gpio write 28 1
   else
    /usr/local/bin/gpio write 27 0
    /usr/local/bin/gpio write 28 0
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
    /usr/local/bin/gpio write 27 1
    /usr/local/bin/gpio write 28 1
   else
    /usr/local/bin/gpio write 27 0
    /usr/local/bin/gpio write 28 0
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
    /usr/local/bin/gpio write 27 1
    /usr/local/bin/gpio write 28 1
   else
    /usr/local/bin/gpio write 27 0
    /usr/local/bin/gpio write 28 0
   fi
  fi


  firstTime=true
 else
  isPressed=false
  firstTimePressed=false

  if [ $countBuzzer -lt 10 ]
  then
   /usr/local/bin/gpio write 27 1
   /usr/local/bin/gpio write 28 1
  else
   /usr/local/bin/gpio write 27 0
   /usr/local/bin/gpio write 28 0

   if [ $countBuzzer -gt 100 ]
   then
    countBuzzer=0
   fi
  fi

  countBuzzer=$(($countBuzzer + 1))
 fi
done
