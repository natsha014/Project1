# Project1

## Описание:

Этот проект предоставляет виджет для работы с банковскими операциями, позволяя фильтровать и сортировать транзакции.

## Установка:

1. Убедись, что у тебя установлен Python версии 3.13.5

2. Клонируй репозиторий

```
git clone https://github.com/username/project-x.git
```

3. Установи зависимости

```
pip install -r requirements.txt
```

## Использование:

Пример использования функций:

```
from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]

# Фильтрация по статусу
executed_ops = filter_by_state(operations)

# Сортировка по дате
sorted_ops = sort_by_date(operations)
```

## Тестирование:

1. Установка Pytest:

```
# Установка через Poetry
poetry add --group dev pytest
```

2. Запуск тестов:

```
# команда для запуска тестов
pytest
```

3. Структура тестов:

тестовые файлы находятся в папке [tests] (./tests)

4. Покрытие тестами:

```
# команда для проверки покрытия тестами
pytest --cov=src --cov-report=html
```

## Генераторы:

```
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Функция поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
usd_transactions = filter_by_currency(transactions, "USD")

# Функция возвращает описание каждой операции по очереди.
descriptions = transaction_descriptions(transactions)

# Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
for card_number in card_number_generator(1, 3):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003

```

## Декоратор:

```

from src.decorators import log

# Декоратор логирования выполнения функции, должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)
   
   ``` 

### Пример использования декоратора:

```

    @log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении:

>>> my_function ok

# Ожидаемый вывод при ошибке:

>>> my_function error: тип ошибки. Inputs: (1, 2), {}

Где тип ошибки заменяется на текст ошибки.
```

## Чтение CSV и Excel файлов

```
from src.read_data import read_csv, read_excel

import pandas as pd

read_csv

# Функция для считывания финансовых операций из CSV принимает путь к файлу CSV 
в качестве аргумента и выдает список словарей с транзакциями.

read_excel

# Функция для считывания финансовых операций из Excel принимает путь к файлу Excel 
в качестве аргумента и выдает список словарей с транзакциями.

```

## Документация:

Для получения дополнительной информации обратитесь к [README](./README.md).