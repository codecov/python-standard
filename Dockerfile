FROM python:3.6

RUN pip install codecov
RUN pip install pytest
RUN pip install pytest-cov
RUN pip install requests

WORKDIR /app
COPY  . /app
