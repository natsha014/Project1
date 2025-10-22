import json
import logging
import os

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_operations(path: str) -> list[dict] | dict:
    """Чтение json файла"""
    logger.info("Запуск функции load_operations")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        logger.error("Файл не существует или пустой")
        return []
    else:
        with open(path, encoding="utf-8") as f:
            oper_file = json.load(f)
            logger.info("Получен писок словарей с данными о финансовых транзакциях")
            if not isinstance(oper_file, list):
                logger.error("Файл не является списком")
                return []
            return oper_file


print(load_operations("../data/operations.json"))
