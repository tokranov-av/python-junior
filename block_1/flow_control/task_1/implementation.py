from typing import (
    Iterable,
)


def get_numbers() -> Iterable[int]:
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    for number in range(1000, 2001):
        if number % 7 == 0 and number % 5 != 0:
            yield number
