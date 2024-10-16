import logging

import requests


def get_exchange_rate():
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        return data["Valute"]["USD"]["Value"]
    except Exception as e:
        logging.error(f"Ошибка при получении курса валют: {e}")
        return "неизвестен"
