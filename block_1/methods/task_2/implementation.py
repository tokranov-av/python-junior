from block_1.common import MyException


class ClassFather:
    """Базовый класс."""

    _name = None
    registered_list = []

    @classmethod
    def get_name(cls):
        if cls._name is None or cls not in cls.registered_list:
            raise MyException

        return cls._name

    @classmethod
    def register(cls):
        if cls._name is None:
            raise MyException

        cls.registered_list.append(cls)


class User1(ClassFather):
    """Дочерний класс 1."""

    _name = "User 1"


class User2(ClassFather):
    """Дочерний класс 2."""

    _name = "User 2"
