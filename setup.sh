#!/bin/bash

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt-get update
sudo apt-get install python3.5 python3-pip python3-virtualenv -y
virtualenv -p /usr/bin/python3.5 ccsep-env
source ccsep-env/bin/activate
pip install -r vuln_requirements.txt
deactivate
echo "Activate virtualenv by typing \'source ccsep-env/bin/activate'"
echo "Deactivate the virtualenv by typing 'deactivate'"
