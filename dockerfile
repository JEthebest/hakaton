FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    postgresql-client

RUN mkdir /app



RUN pip install --no-cache-dir poetry

WORKDIR /app

ADD pyproject.toml poetry.lock poetry.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root
ADD ./ ./

COPY . /app/

CMD python manage.py makemigrations && python manage.py migrate