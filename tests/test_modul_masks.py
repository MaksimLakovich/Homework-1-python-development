import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_positive_mask_card_number(valid_cards_data, expected_valid_cards_data):
    for num in range(len(valid_cards_data)):
        assert get_mask_card_number(valid_cards_data[num]) == expected_valid_cards_data[num]


@pytest.mark.parametrize("card_number",
                         [
                             (70007922896063610000),
                             (700079228960),
                             ("xxxxxxxxxxxxxxxx"),
                             (0000000000000000),
                             ("7000 79** **** 6361"),
                             ("65679228960099X"),
                             ("?#656922860099_"),
                             (),
                         ])
def test_negative_mask_card_number(card_number, fixture_for_none):
    assert get_mask_card_number(card_number) == fixture_for_none


def test_positive_mask_account(valid_account, expected_valid_account):
    for num in range(len(valid_account)):
        assert get_mask_account(valid_account[num]) == expected_valid_account[num]


@pytest.mark.parametrize("account_number",
                         [
                             (736541084301358743050000),
                             (7365410843013587),
                             ("xxxxxxxxxxxxxxxxxxxx"),
                             (00000000000000000000),
                             ("**4305"),
                             ("7365410843013587430X"),
                             ("?#65410843013587430_"),
                             (),
                         ])
def test_negative_mask_account(account_number, fixture_for_none):
    assert get_mask_account(account_number) == fixture_for_none
