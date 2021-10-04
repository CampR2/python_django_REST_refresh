# docker/dockerfile:1

FROM python:3.7-alpine
MAINTAINER Robert Camp (robb2d2)

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user


