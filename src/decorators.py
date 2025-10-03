from functools import wraps
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирования выполнения функции, должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_massage = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_massage)
                else:
                    print(log_massage)
                return result
            except Exception as e:
                error_massage = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_massage)
                else:
                    print(error_massage)

        return inner

    return wrapper
