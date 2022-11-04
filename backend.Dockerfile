FROM python:3.8

WORKDIR app/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


COPY ./pyproject.toml ./pyproject.toml 

RUN bash -c "poetry install --no-root"

COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]
