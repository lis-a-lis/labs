a, b, c = int(input("Введите А:")), int(input("Введите В:")), int(input("Введите С:"))

if a + b > c and a + c > b and c + b > a:
    if max(a, b, c)**2 == (a + b + c - max(a, b, c) - min(a, b, c))**2 + min(a, b, c)**2:
        print("Треугольник существует, яв-ся прямоугольным")
    else:
        print("Треугольник существует, НЕ яв-ся прямоугольным")
else:
    print("Треугольник НЕ существует")

