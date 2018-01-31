#!/bin/bash
. Setenv
cd /home/pi/moyo/ContextServer
sleep 3
#python Switch.py > /dev/null
python Lamp.py > /dev/null

