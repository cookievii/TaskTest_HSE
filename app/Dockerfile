FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .