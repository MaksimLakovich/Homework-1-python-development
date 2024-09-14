from typing import Iterator


def filter_by_currency(transactions_list: list, money: str) -> Iterator[dict]:
    """Функция принимает список словарей (данные о транзакциях) и возвращает итератор,
    который поочередно выдает транзакции с заданной валютой операции (например, USD)"""

    return (entry for entry in transactions_list if entry["operationAmount"]["currency"]["code"] == money)


def transaction_descriptions(transactions_list: list) -> Iterator[str]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for entry in transactions_list:
        yield entry["description"]


def card_number_generator(start: int, finish: int) -> Iterator[str]:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""

    for num in range(start, finish + 1):
        # Преобразовываю число в 16-значную строку с ведущими нулями
        card_number = f"{num:016d}"

        formated_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield formated_card_number
