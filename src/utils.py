import json
import os


def load_operations(path: str) -> list[dict] | dict:
    """Чтение json файла"""
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []
    else:
        with open(path, encoding="utf-8") as f:
            oper_file = json.load(f)
            if not isinstance(oper_file, list):
                return []
            return oper_file
