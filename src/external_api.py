import os

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict) -> float | None:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""

    # Загружаем ключ-api из ".env" через dotenv
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.env")

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
                return float(result["result"])
            except requests.exceptions.RequestException as info:
                print(f"Ошибка при обращении к API: {info}")
                return None  # Возвращаем None, если запрос не удался

        elif transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])

        else:
            print("Валюта транзакции не является USD, EUR или RUB")
            return None  # Возвращаем None, если валюта отличается от USD, EUR или RUB

    else:
        return None  # Возвращаем None, если в транзакции нет 'operationAmount'


# # Пример запуска функции из тек модуля:
# if __name__ == "__main__":
#
#     transaction = {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount":
#             {
#                 "amount": "8221.37",
#                 "currency":
#                     {
#                         "name": "EUR",
#                         "code": "EUR"
#                     }
#             },
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560"
#     }
#
#     result_conversion = get_transaction_amount(transaction)
#
#     print(result_conversion)
