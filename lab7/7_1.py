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
current_x = x0

while current_x < xn:
    current_value = function(current_x)
    if current_value != "-":
        values.append(current_value)
    print(current_x, current_value)
    current_x += hx

print("Sum: ", sum(values))
print("Mult: ", prod(values))
