"""
Что будет выведено после выполнения кода? Почему?
"""


def print_msg(number):

    def printer():
        nonlocal number
        number = 3
        print(number)

    printer()
    print(number)


print_msg(9)

# Ответ:
# 3
# 3

# В функции printer при объявлении переменной number использовано ключевое слово nonlocal
# для обозначения ранее определенных переменных в ближайшей области видимости, исключая глобальную.
