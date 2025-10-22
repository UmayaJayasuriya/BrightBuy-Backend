#!/bin/bash

# Install Python 3
apt-get update
apt-get install -y python3 python3-pip

# Install dependencies
pip3 install -r backend/requirements.txt

# Start backend
uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
