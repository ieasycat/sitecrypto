#!/bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --no-input

gunicorn --bind 0.0.0.0:8000 sitecrypto.wsgi:application
