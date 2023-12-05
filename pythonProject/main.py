from math import *


def function(code):
    x = int(input("Введите Х: "))

    match code:
        case 1:
            return x
        case 2:
            return sqrt(x)
        case 3:
            return exp(1/3 * log(x))
        case 4:
            return sqrt(sqrt(x))
        case _:
            return print("Неправильно выбрана функция")


functions_list = """
Выберите функцию:
1 - y = x
2 - y = sqrt(x)
3 - y = exp(1/3 * ln(x))
4 - y = sqrt(sqrt(x))
>>>
"""

print("Результат:", function(int(input(functions_list))))