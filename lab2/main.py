import math


x = float(input("x >"))
a = float(input("a >"))

z = (x**2 + x / 2) / ( math.exp(x) + math.sin(x)**3 ) + \
    16 * math.exp(x**2) * math.log(x**2)

y = a + x / (7.5 - 3.2 * x**2) + (x**3 * (a - 1)) / math.log(abs(x**3 - 6))

print(
    "z = ", z,
    "y = ", y
)