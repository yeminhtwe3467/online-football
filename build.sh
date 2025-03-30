#!/bin/bash

# Update apt repositories
apt-get update

# Install necessary dependencies for Playwright (without root)
apt-get install

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install Playwright dependencies and browsers
npm install
npx playwright install