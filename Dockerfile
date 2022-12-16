# pull official base image
FROM python:3.11-slim-bullseye

# required by pandas library
RUN apt-get update && apt-get install g++ -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# set work directory
WORKDIR /src/app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

ENV GUNICORN_WORKERS 2
ENV GUNICORN_THREADS 2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /src/app/

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 --workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --access-logfile - --error-logfile - app:server