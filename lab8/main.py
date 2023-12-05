from math import *


def function(x):
    result = 0

    # тк ln при х <= 0 - не существует:
    if x <= 0:
        return "/// Ф-я в данной точке не существует ///"

    for k in range(1, 11):
        result += 1 + k*log(x)

    for n in range(1, 8):
        xpown = 1
        for i in range(1, n + 1):
            xpown *= x

        result += ((x + 1) / 3) * (xpown / 2*n + 1)

    return result


x0 = float(input("X0 >"))
xn = float(input("Xn >"))
hx = float(input("Hx >"))


def round_hx(num):
    return round(num, len(str(hx).split(".")[1]))


current_x = x0
while current_x < xn:
    print(f"F({current_x})={round_hx(function(current_x))}")
    current_x = round_hx(current_x + hx)
