import pytz

from celery import shared_task
from datetime import datetime

from habits.models import Habit
from habits.services import send_tg_message


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
            habit_name = habit.name

            if chat_id:
                send_tg_message(chat_id, habit_name)
                habit.last_reminded = time_now
                habit.save()
