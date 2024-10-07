from typing import Dict, List

from src.filter_descriptions import filter_transaction_by_description


def test_filter_transaction_by_description_found(full_transactions_list: List[Dict]) -> None:
    """Тест на корректную фильтрацию по строке со значением 'пЕреВод'. Использую фикстуру 'full_transactions_list'"""

    input_string = "пЕреВод"

    result = filter_transaction_by_description(full_transactions_list, input_string)

    assert len(result) == 5


def test_filter_transaction_by_description_not_found(full_transactions_list: List[Dict]) -> None:
    """Тест на поиск строки, которой нет в описаниях транзакций. Использую фикстуру 'full_transactions_list'"""

    input_string = "Несуществующая строка"

    result = filter_transaction_by_description(full_transactions_list, input_string)

    assert result == []
