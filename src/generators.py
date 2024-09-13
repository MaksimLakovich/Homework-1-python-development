from typing import Iterator


def filter_by_currency(transactions_list: list, money: str) -> Iterator[dict]:
    """Функция принимает список словарей (данные о транзакциях) и возвращает итератор,
    который поочередно выдает транзакции с заданной валютой операции (например, USD)"""

    return (entry for entry in transactions_list if entry["operationAmount"]["currency"]["code"] == money)


# # Запуск функции напрямую в модуле для проверки работы
# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for entry in range(2):
#         print(next(usd_transactions))


def transaction_descriptions(transactions_list: list) -> Iterator[str]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for entry in transactions_list:
        yield entry["description"]


# # Запуск генератора напрямую в модуле для проверки работы
# if __name__ == "__main__":
#     descriptions = transaction_descriptions(transactions)
#     for entry in range(5):
#         print(next(descriptions))
