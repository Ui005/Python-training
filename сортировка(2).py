# Отсортировать нечетные элементы одномерного массива по возрастанию. Сортировки: «прямой выбор» и быстрая.

import random
import time
from prettytable import PrettyTable
# Подсчёт времени выполнения сортировки
def check_time(array: list, module) -> str:
    start = time.time()
    module(array)
    end = time.time()
    return str(end - start)

#Проверка отсортирован ли массив
def Check(array: list) -> bool:
    return array == sorted(array)

#Быстрая сортировка
def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    else:
        p = random.choice(array)
    left = [i for i in array if i < p]
    right = [i for i in array if i > p]
    mid_nums = [p] * array.count(p)
    array = quick_sort(left) + mid_nums + quick_sort(right)
    if Check(array):
        return array


#Сортировка выбором
def selection_sort(array):
    for i in range(len(array)):
        minimal = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimal]:
                minimal = j
        array[i], array[minimal] = array[minimal], array[i]
    if Check(array):
        return array

#Вывод сравнительной таблицы на экран
def display():
    table = PrettyTable()
    table.field_names = ["Метод", "Частично отсортированная", "Случайная", "Отсортированная в обратном порядке"]
    for i in range(3):
        method_name = ("Быстрая сортировка ","Сортировка прямым выбором", "Встроенная сортировка")
        method = [quick_sort, selection_sort, sorted]
        list = dict()
        list["Метод"] = method_name[i]
        list["Частично отсортированная"] = check_time(array_sort, method[i])
        list["Случайная"] = check_time(array_normal, method[i])
        list["Отсортированная в обратном порядке"] = check_time(array_sort_inv, method[i])

        table.add_row(
            [list["Метод"], list["Частично отсортированная"], list["Случайная"], list["Отсортированная в обратном порядке"]])

    print("количество элементов:" + str(N) + "\n")
    print(table)


N = int(input("введите кол-во элементов последовательности: "))
array_normal = [random.randint(0, 1000) for j in range(N)]
array_sort = sorted(array_normal[:len(array_normal)//2]) + array_normal[len(array_normal)//2:]
array_sort_inv = sorted(array_normal, reverse=True)
display()

