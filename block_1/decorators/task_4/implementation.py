import functools
import time
from typing import (
    Any,
    Callable,
)

from block_1.common import (
    MyException,
    specific_func,
)


def decorator_maker(times: int, delay: int) -> Callable:
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for num in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except AssertionError:
                    print("Не удалось получить валидный результат.", "*" * 50, sep="\n")
                    print(f'Попытка №{num + 1} запуска функции "{func.__name__}"')
                    time.sleep(delay)

            raise MyException("Не удалось получить валидное значение.")

        return wrapper

    return decorator


if __name__ == "__main__":
    result = decorator_maker(times=3, delay=1)(specific_func)()
    print("Результат:", result)
