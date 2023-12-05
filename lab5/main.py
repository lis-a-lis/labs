def function(code):
    match code:
        case 1:
            return 2
        case 2:
            return 2*2
        case 3:
            return 2*2*2
        case 4:
            return 2*2*2*2
        case _:
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