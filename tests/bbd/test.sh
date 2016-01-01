#!/bin/bash

variable=$(mysql -hlocalhost -udgidrone -ppassword dgidrone -e "SELECT * FROM wifiCode")
echo $variable

while read row
do
set $row
echo "$2 $3"
done < <(mysql -hlocalhost -udgidrone -ppassword dgidrone -e "SELECT * FROM wifiCode")
