"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):

    def data_transmitter():
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

# Вывод:
# Test message
# None

# Функция data_transmitter отображает переменную message (выполняется поиск в локальной области видимости,
# объемлющей области видимости)
# Функция transmit_to_space возвращает None, поэтому отобразиться None
