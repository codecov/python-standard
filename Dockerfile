FROM python:3.6

RUN pip install pytest

WORKDIR /app

COPY . /app

RUN py.test