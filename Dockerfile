FROM python:3.12

WORKDIR /bot

COPY poetry.lock pyproject.toml /bot/

RUN pip install poetry
RUN poetry install --no-root

COPY . /bot

CMD ["poetry", "run", "python", "bot.py"]