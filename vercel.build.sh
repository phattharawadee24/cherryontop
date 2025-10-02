#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --noinput