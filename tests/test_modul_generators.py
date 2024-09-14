from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


@pytest.mark.parametrize(
    "start, finish, expected",
    [
        (3493341234, 3493341234, "0000 0034 9334 1234"),
        (35, 35, "0000 0000 0000 0035"),
        (0, 0, "0000 0000 0000 0000"),  # граничное значение
        (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),  # граничное значение
    ],
)
def test_positive_card_number_generator(start: int, finish: int, expected: str) -> None:
    """Тестируем выдачу правильных номеров карт в заданном диапазоне + граничные значения"""

    card_num = card_number_generator(start, finish)

    assert next(card_num) == expected


def test_correct_range_card_number_generator(expected_card_number_for_generator: list[dict[str, Any]]) -> None:
    """Тестируем корректную генерацию номеров карт в заданном диапазоне"""

    card_num = card_number_generator(3493341234, 3493341243)

    # Прохожу по списку ожидаемых значений:
    for expected_card_number in range(len(expected_card_number_for_generator)):
        # Сравниваю каждый элемент из генератора с соответствующим значением фикстуры:
        assert next(card_num) == expected_card_number_for_generator[expected_card_number]
