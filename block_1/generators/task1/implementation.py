from typing import (
    Generator
)


def fib(amount_of_numbers: int) -> Generator[int, None, None]:
    """Возвращает генератор чисел Фибоначчи."""

    num1 = 0
    num2 = 1
    for _ in range(amount_of_numbers):
        num1, num2 = num2, num2 + num1
        yield num1
