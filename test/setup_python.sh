#!/bin/bash

# Created by Kay Men Yap 19257442
# Last updated: 28/09/2020
# Purpose: Set up the python virtual environment to run the test files

sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y
python3 -m venv ccsep-env
source ccsep-env/bin/activate
pip install -r test_requirements.txt
deactivate
echo "Activate virtualenv by typing \'source ccsep-env/bin/activate'"
echo "Deactivate the virtualenv by typing 'deactivate'"
