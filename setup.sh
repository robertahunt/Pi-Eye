#!/bin/bash

# install software needed
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3-pip
sudo apt-get install libatlas-base-dev
sudo apt install python3-opencv

# get latest code
git clone https://github.com/robertahunt/Pi-Eye.git /home/pi/Pi-Eye

# install python modules
python -m pip install bottle
python -m pip install matplotlib
python -m pip install -U numpy

# set up service to run API
sudo groupadd pieye
sudo usermod -G pieye pi
sudo usermod -a -G video pi # after opencv install, seems cannot access camera
sudo cp Pi-Eye/pieye.service /lib/systemd/system/
sudo systemctl enable pieye
sudo systemctl start pieye