# Курсовая работа №7 по блоку "DRF".

Проект представляет собой сервис для управления привычками с отправкой напоминаний в телеграм
с использованием Django и Django REST Framework.


## Установка

1. Клонируйте репозиторий:
   ```bash
    git clone https://github.com/SerjMonstrX/coursework_7_DRF.git
   
2. Установите зависимости, используя Poetry:

       poetry install

3. Настройте PostgreSQL:
Создайте базу данных PostgreSQL, внесите настройки для БД в .env

4. Примените миграции:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

## Структура

Приложение habits содержит модели для привычек

Приложение users содержит реализацию модели юзера.

## Запуск отправки напоминаний в телеграм

Запуск периодических задач рассылок реализован с помощью Celery.
Для начала рассылок запустите Worker и Celery beat.
   ```bash
   celery -A config worker -P eventlet -l info
   celery -A config.celery beat -l info

