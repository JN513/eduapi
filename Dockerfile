FROM python:3.8.3

RUN adduser eduapi

WORKDIR /home/eduapi

RUN apt-get update -y && \
    apt-get install -y \
        cmake \
        git \
        gcc \
        g++ \
RUN apt-get install -y git libffi-dev 
RUN apt-get install -y python3-dev python2 musl-dev postgresql
RUN apt-get install -y  python-pip

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app/ app/
COPY angoera.py config.py ./

ENV FLASK_APP eduapi.py

RUN chown -R eduapi:eduapi ./
USER angoera_api

EXPOSE 8080
CMD venv/bin/gunicorn --bind 0.0.0.0:8080 --access-logfile - --error-logfile - eduapí:app