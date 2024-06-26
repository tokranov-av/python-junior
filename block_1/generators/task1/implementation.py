from typing import (
    Generator
)


def fib(amount_of_numbers: int) -> Generator[int, None, None]:
    """Возвращает генератор чисел Фибоначчи."""
    num1 = 0
    num2 = 1
    while amount_of_numbers:
        num1, num2 = num2, num2 + num1
        yield num1
        amount_of_numbers -= 1
