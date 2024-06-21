import pytz
import requests
from celery import shared_task
from datetime import datetime, timedelta

from config import settings
from habits.models import Habit


@shared_task
def send_telegram_message():
    """Задача для отправки напоминания о привычке"""
    timezone = pytz.UTC
    time_now = datetime.now(timezone)

    habits = Habit.objects.all()

    for habit in habits:
        # Проверяем, нужно ли отправить напоминание
        if habit.last_reminded and habit.last_reminded.date() == time_now.date():
            continue

        if time_now.time() >= habit.time and (not habit.last_reminded or habit.last_reminded.date() != time_now.date()):
            user = habit.creator
            chat_id = user.chat_id
            if chat_id:
                params = {
                    'text': f"Настало время для выполнения привычки: {habit.name}",
                    'chat_id': chat_id,
                }
                requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage', params=params)
                habit.last_reminded = time_now
                habit.save()
