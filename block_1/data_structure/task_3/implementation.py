def copy_dict(origin_dict: dict) -> dict:
    """Функция возвращает копию словаря.

    Для упрощения кода не стал делать копирование для tuple, set и т.д. внутри словаря.
    """
    dict_copy = {}

    def copy_list(origin_list: list) -> list:
        """Функция возвращает копию списка."""
        list_copy = []
        for item in origin_list:
            if isinstance(item, dict):
                item = copy_dict(item)
            elif isinstance(item, list):
                item = copy_list(item)

            list_copy.append(item)

        return list_copy

    for key, value in origin_dict.items():
        if isinstance(value, dict):
            value = copy_dict(value)
        elif isinstance(value, list):
            value = copy_list(value)

        dict_copy[key] = value

    return dict_copy
