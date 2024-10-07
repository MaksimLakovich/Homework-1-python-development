from typing import Generator
from unittest.mock import MagicMock, patch

import pytest

from src.count_transactions import get_categories_number

# Пример набора транзакций для тестов
mocked_transactions = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
]


@pytest.fixture
def mock_get_transactions() -> Generator:
    """Мок для функции get_transactions, возвращающий тестовые данные"""

    with patch("src.utils.get_transactions", return_value=mocked_transactions):
        yield


def test_get_categories_number_with_specific_categories(mock_get_transactions: MagicMock) -> None:
    """Тест с переданными 2-ым аргументом списком конкретных категорий для выборки"""

    categories = ["Открытие вклада", "Перевод организации"]

    result = get_categories_number(mocked_transactions, categories)

    assert result == {"Открытие вклада": 1, "Перевод организации": 1}


def test_get_categories_number_with_empty_categories(mock_get_transactions: MagicMock) -> None:
    """Тест с пустым списком категорий, функция должна вернуть все доступные категории"""

    result = get_categories_number(mocked_transactions, categories=[])

    assert result == {"Перевод организации": 1, "Открытие вклада": 1}


def test_get_categories_number_no_matching_category(mock_get_transactions: MagicMock) -> None:
    """Тест, где категории не совпадают с транзакциями"""

    categories = ["Неизвестная категория"]

    result = get_categories_number(mocked_transactions, categories)

    assert result == {}
