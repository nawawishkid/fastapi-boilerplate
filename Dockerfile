FROM python:3.8

ENV POETRY_VERSION=1.1.6 \
  PATH="${PATH}:/root/.poetry/bin"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version=${POETRY_VERSION}

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . /app

EXPOSE 80

# CMD [ "./bin/start", "--bind", "0.0.0.0:80" ]
CMD [ "poetry", "run", "task", "start", "--bind", "0.0.0.0:80" ]

