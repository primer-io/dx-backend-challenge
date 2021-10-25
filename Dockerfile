FROM python:3.9.1

WORKDIR /code/

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . /code/

EXPOSE 8000

CMD uvicorn main:app --host "0.0.0.0" --port 8000 --reload --no-access-log