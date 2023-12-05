from math import *


def function(x):
    if x < -2:
        return x * x - abs(x + 1)**0.5
    elif -1 < x <= 1:
        return exp(-3 * x*x + 2 * x - 1)
    elif -2 <= x <= -1.5:
        return (sin(x) + cos(x)) / (2 * x + 1)
    else:
        return "-"


x0 = float(input("X0 >"))
xn = float(input("Xn >"))
hx = float(input("Hx >"))

values = []
for i in range(int((xn - x0) / hx)):
    current_value = function(x0 + i * hx)
    if current_value != "-":
        values.append(current_value)
    print(x0 + i * hx, current_value)


print("Sum: ", sum(values))
print("Mult: ", prod(values))
