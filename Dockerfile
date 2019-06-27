FROM python:3.6

RUN pip install codecov \
&& pip install pytest \
&& pip install pytest-cov

WORKDIR /app
COPY . /app
