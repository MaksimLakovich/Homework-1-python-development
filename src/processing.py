def filter_by_state(list_transactions: list, transaction_state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению"""

    return [transaction for transaction in list_transactions if transaction["state"] == transaction_state]


def sort_by_date(list_transactions: list, sort_parameter=True) -> list:
    """Функция возвращает новый список словарей, отсортированный по дате (date) с помощью
    необязательного параметра, задающего порядок сортировки (по умолчанию — убывание)"""

    return [sorted(list_transactions, key=lambda transaction: transaction["date"], reverse=sort_parameter)]
