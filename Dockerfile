# Указываем базовый образ
FROM python:3

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем pyproject.toml и poetry.lock в рабочую директорию
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем все файлы проекта в рабочую директорию
COPY . .
