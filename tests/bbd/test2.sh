#!/bin/bash

while read ok
do
echo $ok
done < <(iwlist wlan0 scan | grep "ESSID:" | sed "s/ESSID:\"\(.*\)\"/\1/g")
