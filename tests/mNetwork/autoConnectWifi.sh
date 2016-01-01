#!/bin/bash -x

fNetworks="networks.list"
fAvailableNetworks="availableNetworks.list"
fWifiConf="/etc/wpa_supplicant/wpa_supplicant.conf"
wifiInterface="wlan0"

alreadyConnected=0

ifdown $wifiInterface
iwlist $wifiInterface scan | grep "ESSID:" | sed "s/ESSID:\"\(.*\)\"/\1/g" > $fAvailableNetworks

if [ -f $fNetworks -a -f $fAvailableNetworks ]
then
	while read network
	do
		set $network
		while read aNetwork
		do
			if [ "k$aNetwork" == "k$1" -a $alreadyConnected -eq 0 ]
			then
				ssid=$1
				shift
				pwd=$*
				echo "equal $aNetwork / $ssid / $pwd"
				cp $fWifiConf old.conf
				#ifconfig $fWifiConf down
				sed "s/\(ssid=\"\).*\(\"\)/\1$ssid\2/" old.conf | sed "s/\(psk=\"\).*\(\"\)/\1$pwd\2/" > $fWifiConf
				#ifdown $wifiInterface
				ifup $wifiInterface
				alreadyConnected=1
			fi
		done < $fAvailableNetworks
	done < $fNetworks
else
	echo "not all files available"
fi
