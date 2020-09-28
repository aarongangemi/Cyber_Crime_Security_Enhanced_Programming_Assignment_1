#!/bin/bash

# Created by Kay Men Yap 19257442
# Last updated: 28/09/2020
# Purpose: To setup the geckodriver needed to run the test files

curl -s -L https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz | tar -xz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin