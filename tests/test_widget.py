import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 3538303347444789556", "Счет Некорректный ввод"),
        ("Visa Platinum 89909221136", "Visa Platinum Некорректный ввод"),
        ("73654108430135874305", " Некорректный ввод"),
        ("Visa Gold", "Visa Некорректный ввод"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(value, expected):
    assert get_date(value) == expected
