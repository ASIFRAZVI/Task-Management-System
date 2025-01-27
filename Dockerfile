FROM python:3-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app/

RUN pip install -r requirement.txt
RUN pip install gunicorn

EXPOSE 8015