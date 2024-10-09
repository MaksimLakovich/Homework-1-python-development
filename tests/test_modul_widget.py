import pytest

from src.widget import get_date, mask_account_card


def test_positive_mask_account_card(valid_name_and_number, expected_valid_name_and_number):
    for num in range(len(valid_name_and_number)):
        assert mask_account_card(valid_name_and_number[num]) == expected_valid_name_and_number[num]


@pytest.mark.parametrize(
    "data",
    [
        ("Счет 3538303347444789556001"),
        ("Счет "),
        ("Visa Classic 700079228960636100"),
        ("Maestro 700079228960"),
        ("Visa Classic 7000 79** **** 6361"),
        ("Visa Platinum 65679228960099X"),
        ("MasterCard ?#656922860099_"),
    ],
)
def test_negative_mask_account_card(data, fixture_for_none):
    assert mask_account_card(data) == fixture_for_none


def test_errors_mask_account_card():
    with pytest.raises(AttributeError) as info_expectation:
        mask_account_card(None)
    assert str(info_expectation.value) == "Некорректный тип данных"


@pytest.mark.parametrize(
    "incoming_date_time, expected",
    [
        ("2024-03-11T02:26:18.671407", "11-03-2024"),
        ("1997-12-01T02:26:18.1", "01-12-1997"),
        (None, None),
        ("", None),
    ],
)
def test_positive_get_date(incoming_date_time, expected):
    assert get_date(incoming_date_time) == expected


@pytest.mark.parametrize(
    "incorrect_date_time",
    [
        ("0000-12-01T02:26:18.1"),
        ("year"),
        ("2024-03-11T02"),
        ("2024-00-11T02:26:18.671407"),
        ("??24-03-11T02:26:18.671407"),
        ("2024-03-00T02:26:18.671407"),
        ("2024-03-11"),
    ],
)
def test_errors_get_date(incorrect_date_time):
    # with pytest.raises(ValueError):
    #     get_date(incorrect_date_time)
    assert get_date(incorrect_date_time) is None
