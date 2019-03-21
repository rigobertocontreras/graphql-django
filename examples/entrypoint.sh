#!/bin/sh
python manage.py migrate auth
python manage.py makemigrations
python manage.py migrate
exec "$@"