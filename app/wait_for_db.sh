#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate

# below line is to tell to continue the rest of the build flow
exec "$@"