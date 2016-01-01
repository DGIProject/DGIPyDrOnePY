#!/bin/sh

file=$1

if [ -f $file ]
then
 while read line
 do
  kill -9 $line
 done < $file

 rm $1
else
 echo "not already started"
fi
