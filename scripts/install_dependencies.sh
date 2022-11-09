#!/bin/bash

sudo apt-get update
sudo apt-get install -y virtualenv python3 python3-pip
pip install Flask
pip install -r requirements.txt
