from calendar import (
    monthrange,
)
from datetime import (
    datetime,
)


def get_days_count_by_month(month_name: str) -> int:
    """Возвращает количество дней по месяцу

    Args:
        month_name: название месяца

    Returns: количество дней
    """
    days = 0
    current_year = datetime.now().year
    months = {
        "январь": 1,
        "февраль": 2,
        "март": 3,
        "апрель": 4,
        "май": 5,
        "июнь": 6,
        "июль": 7,
        "август": 8,
        "сентябрь": 9,
        "октябрь": 10,
        "ноябрь": 11,
        "декабрь": 12,
    }
    month_num = months.get(month_name.strip().lower())
    if month_num:
        days = monthrange(current_year, month_num)[1]

    return days
