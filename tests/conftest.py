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
def fixture_for_none():
    return None
