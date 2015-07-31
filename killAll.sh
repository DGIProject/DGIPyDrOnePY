#!/bin/sh

file="pid.log"

if [ -f $file ]
then
 while read line
 do
  kill $line
 done < $file

 rm pid.log
else
 echo "not already started"
fi
