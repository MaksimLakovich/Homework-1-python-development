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


@pytest.fixture
def valid_list_transactions():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def filtered_by_executed():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.fixture
def filtered_by_canceled():
    return [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]


@pytest.fixture
def sorted_with_reverse():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.fixture
def sorted_without_reverse():
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    ]


@pytest.fixture
def list_transactions_with_same_dates():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:00:00.1'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:00:00.11'},
    ]


@pytest.fixture
def sorted_with_reverse_with_same_dates():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:00:00.11'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:00:00.1'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
