#!/bin/bash

# Update apt repositories
apt-get update

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install Playwright dependencies and browsers
npx playwright install --with-deps