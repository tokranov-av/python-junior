from typing import (
    Literal,
    Union,
)


def convert_temperature(
    value: Union[int, float], to_scale: Literal["F", "C"]
) -> Union[int, float]:
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if to_scale == "C":
        t = 5 / 9 * (value - 32)
    elif to_scale == "F":
        t = 9 / 5 * value + 32
    else:
        t = value

    return t
