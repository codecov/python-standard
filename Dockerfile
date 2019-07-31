FROM python:3.6-alpine

RUN pip install codecov
RUN pip install pytest
RUN pip install pytest-cov
RUN pip install requests

WORKDIR /app
COPY . /app

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]