#! /bin/bash
cd /home/pi/thermo
nohup python ./manage.py runserver 0.0.0.0:80 --noreload &
