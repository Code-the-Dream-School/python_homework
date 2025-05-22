#!/bin/bash

# Install Chromium and dependencies
sudo apt update
sudo apt install -y chromium-browser chromium-chromedriver

# Set environment variables to help Selenium find the browser
echo 'export CHROME_BIN=/usr/bin/chromium-browser' >> ~/.bashrc
echo 'export PATH=$PATH:/usr/lib/chromium-browser/' >> ~/.bashrc
source ~/.bashrc

# Verify installations
which chromium-browser
chromium-browser --version
chromedriver --version
