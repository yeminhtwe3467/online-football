#!/bin/bash

mkdir -p /home/render/.cache  # Ensure the cache directory exists
pip install -r requirements.txt  # Install dependencies
playwright install  # Install Playwright browsers