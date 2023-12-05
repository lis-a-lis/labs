from math import *


def function(code, x):
    if code == 1:
        return x
    elif code == 2:
        return sqrt(x)
    elif code == 3:
        return exp(1/3 * log(x))
    elif code == 4:
        return sqrt(sqrt(x))
    else:
        return "Неправильно выбрана функция"


functions_list = """
Выберите функцию:
1 - y = x
2 - y = sqrt(x)
3 - y = exp(1/3 * ln(x))
4 - y = sqrt(sqrt(x))
>>>
"""

print("Результат:", function(int(input(functions_list)), int(input("Введите Х: "))))