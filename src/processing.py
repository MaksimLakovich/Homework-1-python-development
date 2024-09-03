def filter_by_state(list_transactions: list, transaction_state="EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению"""

    return [transaction for transaction in list_transactions if transaction["state"] == transaction_state]
