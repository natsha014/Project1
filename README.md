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

## Документация:

Для получения дополнительной информации обратитесь к [README](./README.md).