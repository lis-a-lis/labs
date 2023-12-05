def function_1(x):
    return 3*x**3 + 2*x**2 + x + 5


def function_2(x):
    return 2*x**3 - 4*x**2 + 2*x - 5


x0 = float(input("X0 >"))
xn = float(input("Xn >"))
hx = float(input("Hx >"))

distances = []
current_x = x0

while current_x < xn:
    distances.append(function_1(current_x) - function_2(current_x))
    current_x += hx

print(f"Минимальное расстояние между ф-ей 1 и 2: {min(distances)}")
print(f"Максимальное расстояние между ф-ей 1 и 2: {max(distances)}")
