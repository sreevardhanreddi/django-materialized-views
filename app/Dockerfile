# pull official base image
FROM python:3.8-buster

# set work directory
RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 and Pillow dependencies
RUN apt-get update && apt-get install -y apt-transport-https apt-utils netcat
RUN apt-get install libpq-dev gcc python3-dev musl-dev python3-pip -y

# install dependencies
COPY ./requirements.txt .
# upgrade pip
RUN pip install pip
RUN pip install -r requirements.txt

# copy wait_for_db.sh
COPY ./wait_for_db.sh .

# copy project
COPY . .

ENTRYPOINT ["/app/wait_for_db.sh"]

CMD python manage.py runserver 0.0.0.0:8000