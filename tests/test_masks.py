import pytest

from src.masks import get_mask_card, get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2600376529871290", "2600 37** **** 1290"),
        ("123", "Некорректный ввод"),
        ("asdfghjkqwercvbn", "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_get_mask_card(value, expected):
    assert get_mask_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("26003765298712341290", "**1290"),
        ("123", "Некорректный ввод"),
        ("asdfghjkqwercvbnфыва", "Некорректный ввод"),
        ("", "Некорректный ввод"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
