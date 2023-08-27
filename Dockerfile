FROM python:3.11-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src
COPY main.py /app/

CMD ["tail", "-f", "/dev/null"]
