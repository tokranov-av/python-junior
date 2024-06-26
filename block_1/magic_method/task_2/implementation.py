from datetime import (
    datetime,
    timedelta,
)


class MathClock:
    def __init__(self):
        self.__now = datetime.now()
        self.__clock = datetime(
            year=self.__now.year,
            month=self.__now.month,
            day=self.__now.day,
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

    def get_time(self) -> str:
        return self.__clock.strftime("%H:%M")

    def __add__(self, other: int):
        self.__clock += timedelta(minutes=other)

    def __sub__(self, other: int):
        self.__clock -= timedelta(minutes=other)

    def __mul__(self, other: int):
        self.__clock += timedelta(hours=other)

    def __truediv__(self, other: int):
        self.__clock -= timedelta(hours=other)
