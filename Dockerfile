FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV CGO_ENABLED 1

WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY src .
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-interaction --no-ansi --no-root
# RUN echo $(ls -a)
# COPY src/app /app
