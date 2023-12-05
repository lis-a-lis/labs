import math


x = eval(input("Введите Х (pi записывать как math.pi): "))

if ((-math.pi / 2) > x) or x > 0:
    print("undefined")
else:
    if (-math.pi / 2) <= x <= (-math.pi / 4):
        print("f=", 2*math.sin(math.pi / 4 - x / 2)**2)
    if (-math.pi / 4) < x < (-math.pi / 8):
        print("f=", (1 - math.cos(2*x)) / math.sin(2*x))
    if (-math.pi / 8) <= x <= 0:
        print("f=", x / (2 + math.cos(x)))

