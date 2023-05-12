FROM python:3.11.3-alpine3.17

WORKDIR /django_project

ENV PYTHONUNBUFFERED 1
ENV DB_HOST_DOCKER="db"


RUN apk add postgresql-client build-base postgresql-dev
COPY requirements.txt /django_project
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .
