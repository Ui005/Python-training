"""
Gрограмма, которая:
запрашивает у пользователя размер массива и ключ поиска;
формирует массив случайных чисел;
возвращает количество совпадений и их номера.
"""
import random
from random import randint
n = int(input("Введите размер массива: "))
k = int(input("введите число, которое нужно найти: "))
array = [random.randint(-10,10) for i in range(n)]
b = []
for i in range(len(array)):
    if array[i] == k:
        b.append(i)

print("массив: ", array)
if len(b) == 0:
    print("Числа нет в массиве")
else:
    print("Число", k, "встречается в массиве ", len(b), " раз и соответствует индексам", b)