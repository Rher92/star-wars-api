#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

cd star_wars
python manage.py migrate
python manage.py runserver 0.0.0.0:8000