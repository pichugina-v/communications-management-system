FROM python:3.10-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

RUN #poetry export -f requirements.txt --output requirements.txt --without-hashes

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

WORKDIR  /app

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

RUN poetry install --only main

COPY . .
