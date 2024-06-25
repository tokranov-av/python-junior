from typing import (
    Union,
)

from block_1.common import (
    MyException,
)


class Value:
    def __init__(self, value: Union[int, float]):
        self.value = value

    def __add__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно складывать только с числом")

        return self.value + other

    def __radd__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно складывать только с числом")

        return self.value + other

    def __sub__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно вычитать только число")

        return self.value - other

    def __rsub__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно вычитать только из числа")

        return other - self.value

    def __mul__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно умножать только на число")

        return self.value * other

    def __rmul__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно умножать только на число")

        return self.value * other

    def __truediv__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно делить только на число")
        if other == 0:
            raise MyException("Нельзя делить на 0")

        return self.value / other

    def __rtruediv__(self, other: Union[int, float]) -> Union[int, float]:
        if not isinstance(other, (int, float)):
            raise MyException("Можно делить только число")

        return other / self.value
