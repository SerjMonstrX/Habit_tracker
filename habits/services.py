import requests
from config import settings


def send_tg_message(chat_id, habit):
    params = {
        'text': f"Настало время для выполнения привычки: {habit}",
        'chat_id': chat_id
    }
    requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage', params=params)
