import pytest

from src.process_bank import process_bank_operations
from src.process_bank import process_bank_search


@pytest.fixture
def transactions():
    return [
        {"description": "Перевод со счета на счет", "amount": 100},
        {"description": "Перевод со счета на счет", "amount": 200},
        {"description": "Открытие вклада", "amount": 150},
        {"description": "Перевод организации", "amount": 300},
        {"description": "Перевод с карты на карту", "amount": 250},
        {"description": "Открытие вклада", "amount": 500},
    ]


@pytest.mark.parametrize(
    "search_str, expected",
    [
        (
            "перевод",
            [
                {"description": "Перевод со счета на счет", "amount": 100},
                {"description": "Перевод со счета на счет", "amount": 200},
                {"description": "Перевод организации", "amount": 300},
                {"description": "Перевод с карты на карту", "amount": 250},
            ],
        ),
        (
            "счет",
            [
                {"description": "Перевод со счета на счет", "amount": 100},
                {"description": "Перевод со счета на счет", "amount": 200},
            ],
        ),
        (
            "вклад",
            [{"description": "Открытие вклада", "amount": 150}, {"description": "Открытие вклада", "amount": 500}],
        ),
        ("организации", [{"description": "Перевод организации", "amount": 300}]),
        ("карта", []),
    ],
)
def test_process_bank_search(transactions, search_str, expected):
    assert process_bank_search(transactions, search_str) == expected


@pytest.mark.parametrize(
    "categories, expected",
    [
        ("Строка", {}),
        ([], {}),
        (["Закрытие вклада", "Оплата счета"], {}),
        (
            ["Перевод организации", "Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту"],
            {
                "Перевод организации": 1,
                "Открытие вклада": 2,
                "Перевод со счета на счет": 2,
                "Перевод с карты на карту": 1,
            },
        ),
        (
            ["Перевод организации", "Открытие вклада", "Закрытие вклада", "Оплата счета"],
            {"Перевод организации": 1, "Открытие вклада": 2},
        ),
    ],
)
def test_process_bank_operations(transactions, categories, expected):
    assert process_bank_operations(transactions, categories) == expected
