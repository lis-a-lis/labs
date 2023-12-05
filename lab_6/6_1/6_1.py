from math import *
import random


def calculate_a(n):
    b = random.randint(1, 128)
    return pow(1 + b, 1 / n)


n = int(input("Выберите, сколько элементов последовательности вывести(n): "))

for i in range(n):
    print(f"a{i} = {calculate_a(n)}")
