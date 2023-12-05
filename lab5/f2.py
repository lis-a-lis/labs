def function(code):
    if code == 1:
        return 2
    elif code == 2:
        return 2*2
    elif code == 3:
        return 2*2*2
    elif code == 4:
        return 2*2*2*2
    else:
        return "Неправильно выбрана функция"


functions_list = """
Выберите функцию:
1 - y = 2
2 - y = 2*2
3 - y = 2*2*2
4 - y = 2*2*2*2
>>>
"""

print("Результат:", function(int(input(functions_list))))