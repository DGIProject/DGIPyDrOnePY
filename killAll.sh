#!/bin/sh

while read line
do
   kill $line
done < pid.log

rm pid.log
