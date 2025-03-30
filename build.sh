#!/bin/bash

# Install system dependencies for Playwright
apt-get update
apt-get install -y wget ca-certificates fonts-liberation libappindicator3-1 libnss3 libxss1 libxtst6 xdg-utils

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers with dependencies
npx playwright install --with-deps