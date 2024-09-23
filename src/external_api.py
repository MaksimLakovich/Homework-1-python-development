import os
from typing import Iterator, Optional

import requests
from dotenv import load_dotenv

from src.utils import get_transactions


def get_transaction_amount(path: str) -> Iterator[Optional[float]]:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""

    # Загружаем ключ-api из ".env" через dotenv
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.env")

    # Открываем файл-json с транзакциями через функцию чтения get_transactions() в модуле util.py
    transactions_list_from_json = get_transactions(path)

    for transaction in transactions_list_from_json:
        if "operationAmount" in transaction:

            # Конвертация валюты при необходимости
            if transaction["operationAmount"]["currency"]["code"] in ["EUR", "USD"]:
                url = "https://api.apilayer.com/exchangerates_data/convert"
                payload = {
                    "amount": transaction["operationAmount"]["amount"],
                    "from": transaction["operationAmount"]["currency"]["code"],
                    "to": "RUB",
                }
                headers = {"apikey": api_key}

                # Получаем результат amount по транзакциям в USD или EUR после конвертации в RUB
                try:
                    response = requests.request("GET", url, headers=headers, params=payload)
                    response.raise_for_status()  # Поднимаем исключение, если произошла ошибка
                    result = response.json()
                    yield float(result["result"])
                except requests.exceptions.RequestException as info:
                    print(f"Ошибка при обращении к API: {info}")
                    yield None  # Возвращаем None, если запрос не удался

            else:
                yield float(transaction["operationAmount"]["amount"])


# # Пример запуска функции из тек модуля:
# if __name__ == "__main__":
#     PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     transaction = get_transaction_amount(PATH_TO_FILE)
#     print(next(transaction))
#     print(next(transaction))
#     print(next(transaction))
