# Курсовая работа №7 по блоку "DRF".

Проект представляет собой сервис для управления привычками с отправкой напоминаний в телеграм
с использованием Django и Django REST Framework.


## Установка
1. Установаите Docker.
2. Клонируйте репозиторий:
   ```bash
    git clone https://github.com/SerjMonstrX/coursework_7_DRF.git

3. Внесите настройки в файл .env

4. Запустите проект командой:
      ```bash
      docker-compose up -d --build

## Структура

Приложение habits содержит модели для привычек, для управления реализован механизм CRUD.

Пример создания привычки:

        habit_data_1 = {
            'name': 'Test Habit',
            'place': 'Дома',
            'time': '12:00:00',
            'action': 'Почитать книгу',
            'is_pleasant': False,
            'frequency': 1,
            'reward': 'Скушать конфету',
            'time_to_complete': 30,
            'is_public': False,
        }




Приложение users содержит реализацию модели юзера.

Для получения напоминаний от телеграм бота необходимо при создании пользователя указать chat_id в поле chat_id.

      {
       "email": "user@example.com",
       "password": "password123",
       "chat_id": "your_chat_id_here"
      }


## Запуск отправки напоминаний в телеграм

Запуск периодических задач рассылок реализован с помощью Celery.
   
      celery -A config worker -P eventlet -l info
      celery -A config.celery beat -l info

## Документация
Для проекта настроен вывод документации через swagger или redoc

      http://127.0.0.1:8000/swagger/

      http://127.0.0.1:8000/redoc/


