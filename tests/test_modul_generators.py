from typing import Any

import pytest

from src.generators import filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "money, expected_fixture",
    [
        ("USD", "usd_expected_list"),
        ("RUB", "rub_expected_list"),
    ],
)
def test_positive_filter_by_currency(
    full_transactions_list: list[dict[str, Any]], request: pytest.FixtureRequest, money: str, expected_fixture: str
) -> None:
    """Тестируем позитивные случаи когда на входе и на выходе есть данные"""

    expected = request.getfixturevalue(expected_fixture)
    assert list(filter_by_currency(full_transactions_list, money)) == list(expected)


def test_empty_transactions_list() -> None:
    """Тестируем кейс с пустым списком на входе"""

    assert list(filter_by_currency(transactions_list=[], money="USD")) == list([])


def test_with_not_exist_money(full_transactions_list: list[dict[str, Any]]) -> None:
    """Тестируем кейс с запросом выборки в валюте, транзакций по которой нет в списке"""

    result = filter_by_currency(full_transactions_list, money="UAH")
    with pytest.raises(StopIteration):
        next(result)


def test_positive_transaction_descriptions(full_transactions_list: list[dict[str, Any]]) -> None:
    """Тестируем позитивные случаи поочередного получения descriptions каждой транзакции"""

    description = transaction_descriptions(full_transactions_list)

    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"
