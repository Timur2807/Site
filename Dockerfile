FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt req.txt

RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY my_site .