import json
import logging
import os

logger = logging.getLogger("utils")
logging.basicConfig(
    level=logging.DEBUG,
    filename=os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log"),
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)


def load_operations(path: str) -> list[dict] | dict:
    """Чтение json файла"""
    logger.info("Запуск функции load_operations")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        logger.error("Файл не существует или пустой")
        return []
    else:
        with open(path, encoding="utf-8") as f:
            oper_file = json.load(f)
            logger.info("Получен список словарей с данными о финансовых транзакциях")
            for i in oper_file:
                # Проверяем и разворачиваем вложенные данные
                if "operationAmount" in i: #pragma: no cover
                    i["amount"] = i["operationAmount"]["amount"]
                    i["currency_name"] = i["operationAmount"]["currency"]["name"]
                    i["currency_code"] = i["operationAmount"]["currency"]["code"]
                    # Удаляем вложенный элемент, если больше не нужен
                    del i["operationAmount"]

            if not isinstance(oper_file, list):
                logger.error("Файл не является списком")
                return []
            return oper_file
