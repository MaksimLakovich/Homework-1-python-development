from typing import Iterator


def filter_by_currency(transactions_list: list, money: str) -> Iterator[dict]:
    """Функция принимает список словарей (данные о транзакциях) и возвращает итератор,
    который поочередно выдает транзакции с заданной валютой операции (например, USD)."""

    return (entry for entry in transactions_list if entry["operationAmount"]["currency"]["name"] == money)


# # Запуск функции напрямую в модуле для проверки работы
# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for entry in range(2):
#         print(next(usd_transactions))
