class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args):
        self.data = tuple(args)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, key, value):
        raise TypeError

    def __delitem__(self, key):
        raise TypeError

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        cnt = 0
        for item in self.data:
            if item == value:
                cnt += 1

        return cnt

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """
        for index, val in enumerate(self.data):
            if value == val:
                return index

        raise ValueError
