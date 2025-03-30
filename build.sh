#!/bin/bash

# Update apt repositories
apt-get update

# Install necessary dependencies for Playwright (without root)
apt-get install -y wget fonts-liberation libappindicator3-1 libnss3 libxss1 libxtst6 xdg-utils

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install Playwright dependencies and browsers
npx playwright install