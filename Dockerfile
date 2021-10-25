FROM python:3.9.1

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry && \
    poetry config settings.virtualenvs.create false && \
    poetry install

COPY . /

EXPOSE 8000

CMD uvicorn core_api.api.merchant.main:app --host "0.0.0.0" --port 8000 --reload --no-access-log