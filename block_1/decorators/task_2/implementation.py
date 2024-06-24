import functools
from typing import (
    Callable,
)

from block_1.common import (
    MyException,
    factorial,
)
from block_1.decorators.task_1.implementation import (
    time_execution,
)

CACHED_RESULTS = {}


def check_value(func: Callable) -> Callable:
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """

    @functools.wraps(func)
    def wrapper(number: int) -> int:
        if isinstance(number, int) and number < 0:
            raise MyException("Переданное значение должно быть неотрицательное число!")
        if not isinstance(number, int):
            raise MyException("Передаваемое значение должно быть типа int")

        return func(number)

    return wrapper


def cache(func: Callable) -> Callable:
    """Декоратор кэширующий результат."""

    @functools.wraps(func)
    def wrapper(number: int) -> int:
        if number in CACHED_RESULTS:
            res = CACHED_RESULTS[number]
        else:
            res = func(number)
            CACHED_RESULTS[number] = res

        return res

    return wrapper


if __name__ == "__main__":
    print(time_execution(cache(factorial))(100))
    print("*" * 50)
    print(time_execution(cache(factorial))(100))
    print("*" * 50)
    print(check_value(factorial)(-10))
