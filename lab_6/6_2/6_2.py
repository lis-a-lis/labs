def calculate_ln(x):
    result = 0
    for n in range(0, 10):
        result += ((x - 1) ** (2 * n - 1)) / (2 * n + 1) * ((x + 1) ** (2 * n + 1))

    return 2 * result


a = float(input("a > "))
x = float(input("x > "))

z = a * calculate_ln(x) if x >= a else x * calculate_ln(a)

print(z)

