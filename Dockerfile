FROM python:3.12-alpine

RUN apk add --no-cache gcc musl-dev linux-headers zlib-dev postgresql-dev

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install --no-root

COPY . /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]