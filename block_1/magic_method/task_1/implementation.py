from typing import (
    Union,
)


class Multiplier:
    MULTIPLIER = 1

    def __init__(self, value: Union[int, float]):
        self._value = value * self.MULTIPLIER

    def get_value(self) -> Union[int, float]:
        return self._value

    def __str__(self):
        return str(self._value)

    def __add__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value + other._value)

    def __radd__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value + other._value)

    def __iadd__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value + other._value)

    def __sub__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value - other._value)

    def __rsub__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(other._value - self._value)

    def __isub__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value - other._value)

    def __mul__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value * other._value)

    def __rmul__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value * other._value)

    def __truediv__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(self._value / other._value)

    def __rtruediv__(self, other: "Multiplier") -> "Multiplier":
        return Multiplier(other._value / self._value)

    def __eq__(self, other: "Multiplier") -> bool:
        return self._value == other._value

    def __ne__(self, other: "Multiplier") -> bool:
        return self._value != other._value

    def __gt__(self, other: "Multiplier") -> bool:
        return self._value > other._value

    def __lt__(self, other: "Multiplier") -> bool:
        return self._value < other._value

    def __ge__(self, other: "Multiplier") -> bool:
        return self._value >= other._value

    def __le__(self, other: "Multiplier") -> bool:
        return self._value <= other._value


class Hundred(Multiplier):
    """Множитель на 100."""

    MULTIPLIER = 100


class Thousand(Multiplier):
    """Множитель на 1 000."""

    MULTIPLIER = 1000


class Million(Multiplier):
    """Множитель на 1 000 000."""

    MULTIPLIER = 1000000
