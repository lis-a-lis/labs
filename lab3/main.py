def f(a, n, x):
    return a * x**n


x = int(input("Введите Х: "))

p = (f(8, 4, x) + f(7.5, 2, x) - 4) / (f(5.3, 3, x) + x + 3)
q = (f(5, 5, x) + 3) / (f(1, 2, x) + 1)

print("P(x)=", p)
print("Q(x)=", q)
