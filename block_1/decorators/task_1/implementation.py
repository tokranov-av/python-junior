import functools
import time
from typing import (
    Any,
    Callable,
)

from block_1.common import (
    factorial,
)


def time_execution(func: Callable) -> Callable:
    """Обертка, печатающая время выполнения функции."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        time_start = time.perf_counter()
        res = func(*args, **kwargs)
        lead_time = time.perf_counter() - time_start
        print(f'Время выполнения функции "{func.__name__}" составило {lead_time:.6f}c')

        return res

    return wrapper


if __name__ == "__main__":
    result = time_execution(factorial)(100)
    print(result)
