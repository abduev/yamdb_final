FROM python:3.8-slim

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000