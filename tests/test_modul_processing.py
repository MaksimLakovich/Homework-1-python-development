import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "transaction_state, expected_fixture",
    [
        ("EXECUTED", "filtered_by_executed"),
        ("CANCELED", "filtered_by_canceled"),
        ("", []),
        (None, []),
        ("NOT", []),
    ],
)
def test_filter_by_state(valid_list_transactions, request, transaction_state, expected_fixture):
    if isinstance(expected_fixture, str):
        expected = request.getfixturevalue(expected_fixture)
        assert filter_by_state(valid_list_transactions, transaction_state) == expected
    else:
        expected = expected_fixture
        assert filter_by_state(valid_list_transactions, transaction_state) == expected


@pytest.mark.parametrize(
    "sort_parameter, expected_fixture", [(True, "sorted_with_reverse"), (False, "sorted_without_reverse")]
)
def test_sort_by_date(valid_list_transactions, request, sort_parameter, expected_fixture):
    expected = request.getfixturevalue(expected_fixture)
    assert sort_by_date(valid_list_transactions, sort_parameter) == expected


@pytest.mark.parametrize(
    "sort_parameter, expected_fixture",
    [
        (True, "sorted_with_reverse_with_same_dates"),
    ],
)
def test_sort_with_same_dates(list_transactions_with_same_dates, request, sort_parameter, expected_fixture):
    expected = request.getfixturevalue(expected_fixture)
    assert sort_by_date(list_transactions_with_same_dates, sort_parameter) == expected
