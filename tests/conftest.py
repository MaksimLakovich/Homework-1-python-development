import pytest


@pytest.fixture
def valid_cards_data():
    return [
        7000792289606361,
        "6456792289600998",
        None,
    ]


@pytest.fixture
def expected_valid_cards_data():
    return [
        "7000 79** **** 6361",
        "6456 79** **** 0998",
        None,
    ]


@pytest.fixture
def valid_account():
    return [
        73654108430135874305,
        "70011087771342305433",
        None,
    ]


@pytest.fixture
def expected_valid_account():
    return [
        "**4305",
        "**5433",
        None,
    ]


@pytest.fixture
def valid_name_and_number():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "Visa Classic 6831982476737658",
    ]


@pytest.fixture
def expected_valid_name_and_number():
    return [
        "Maestro 1596 83** **** 5199",
        "Счет **9589",
        "Visa Classic 6831 98** **** 7658",
    ]


@pytest.fixture
def fixture_for_none():
    return None
