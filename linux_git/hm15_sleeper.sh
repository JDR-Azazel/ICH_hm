#!/bin/bash

	for i in {1..10}
	do
	date +"%H:%M:%S"
	ps -ef | wc -l
	sleep 3
	done

cat /proc/cpuinfo >> hm15.txt
cat /etc/os-release | head -1 >> hm15.txt 
cat /etc/os-release | head -1 | sed 's/^NAME="\(.*\)"$/\1/' >> hm15.txt

	for i in {50..100} 
	do 	
	touch $i.txt
	done
