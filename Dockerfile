FROM python:3

ENV PYTHONNUNBUFFERED 1

WORKDIR /myapp

ADD . /myapp

COPY . /requirements.txt /myapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /myapp 