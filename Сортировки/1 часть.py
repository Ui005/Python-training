"""
Программа, которая подключает модуль sorts.py(написанный самостоятельно) и сортирует  3 последовательности:
отсортированную, случайно сгенерированную (при помощи встроенных средств соответствующей системы программирования)
и отсортированную в обратном порядке, тремя различными методами сортировки .
Время выполнения в каждом случае подсчитывается и выводитсяя  на экран в виде таблицы для анализа методов.

Входные данные: вводятся с клавиатуры
N - число элементов последовательностей;

Выходные данные: выводятся в файл output.txt.
"""

from sorts import *
import random
import time
from prettytable import PrettyTable
from copy import deepcopy


N = int(input("введите кол-во элементов последовательности: "))
array_normal = [random.randint(0, 1000) for j in range(N)]
array_copy = deepcopy(array_normal)
array_sort = sorted(array_normal)
array_sort_inv = sorted(array_normal, reverse=True)


def check_time(array: list, module) -> str:
    start = time.time()
    module(array)
    end = time.time()
    return str(end - start)


def file_write():
    table = PrettyTable()
    table.field_names = ["Метод", "Отсортированная", "Случайная", "Отсортированная в обратном порядке"]
    for i in range(3):
        method_name = ("Обменная сортировка", "Сортировка слиянием", "Быстрая сортировка ", "Встроенная сортировка")
        method = [bubble, merge, quick_sort, sorted]
        list = dict()
        list["Метод"] = method_name[i]
        list["Отсортированная"] = check_time(array_sort, method[i])
        list["Случайная"] = check_time(array_normal, method[i])
        list["Отсортированная в обратном порядке"] = check_time(array_sort_inv, method[i])

        table.add_row(
            [list["Метод"], list["Отсортированная"], list["Случайная"], list["Отсортированная в обратном порядке"]])

    with open("output.txt", "w", encoding='utf-8') as f:
        f.write("количество элементов:" + str(N) + "\n")
        f.write("случайная последовательность, сгенерированная программно:" + str(array_copy) + "\n")
        f.write(str(table))

if Check(array_sort) and not(Check(array_normal)) and not(Check(array_sort_inv)):
    file_write()
