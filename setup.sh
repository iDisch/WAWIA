#!/bin/bash
virtualenv venv
source venv/bin/activate
pip install django
python manage.py migrate