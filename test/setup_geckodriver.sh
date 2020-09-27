#!/bin/bash

curl -s -L https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz | tar -xz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin