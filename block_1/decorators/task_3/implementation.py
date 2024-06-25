import functools
from collections import (
    Counter,
)
from typing import (
    Callable,
)

from block_1.common import (
    some_func,
)

number_of_calls = Counter()


def counter(func: Callable) -> Callable:
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        func(*args, **kwargs)
        number_of_calls[id(func)] += 1

        return number_of_calls[id(func)]

    return wrapper


if __name__ == "__main__":
    print(counter(some_func)())
    print(counter(some_func)())
    print(counter(some_func)())
