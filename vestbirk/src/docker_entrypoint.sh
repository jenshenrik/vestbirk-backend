#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata guilds/initial_data.json

# Start gunicorn processes
echo Starting Gunicorn
exec gunicorn vestbirk.wsgi:application \
    --name vestbirk-django \
    --bind 0.0.0.0:8000 \
    --log-level=info
