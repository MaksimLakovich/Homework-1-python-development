import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import fixture_none


@pytest.mark.parametrize("card_number, expected",
                         [
                             (7000792289606361, "7000 79** **** 6361"),
                             ("6456792289600998", "6456 79** **** 0998"),
                         ])
def test_mask_card_positive(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number",
                         [
                             (70007922896063610000),
                             (700079228960),
                             (None),
                             ("xxxxxxxxxxxxxxxx"),
                             (0000000000000000),
                             ("7000 79** **** 6361"),
                             ("65679228960099X"),
                             ("?#656922860099_")
                         ])
def test_mask_card_negative(card_number, fixture_none):
    assert get_mask_card_number(card_number) == fixture_none


@pytest.mark.parametrize("account_number, expected",
                         [
                             (73654108430135874305, "**4305"),
                             ("73654108430135874305", "**4305"),
                         ])
def test_mask_account_positive(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number",
                         [
                             (736541084301358743050000),
                             (7365410843013587),
                             (None),
                             ("xxxxxxxxxxxxxxxxxxxx"),
                             (00000000000000000000),
                             ("**4305"),
                             ("7365410843013587430X"),
                             ("?#65410843013587430_")
                         ])
def test_mask_account_negative(account_number, fixture_none):
    assert get_mask_account(account_number) == fixture_none
