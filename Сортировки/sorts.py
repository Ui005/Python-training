"Методы сортировки"
import random

def Check(array: list) -> bool:
    return array == sorted(array)

def bubble(array: list) -> list:                        #Обменная сортировка
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]
    if Check(array):
        return array

def get_merge(left: list, right: list) -> list:         #Сортировка слиянием
    sort_array = []
    len_left, len_right = len(left), len(right)
    left_index = right_index = 0
    for i in range(len_right + len_left):
        if left_index < len_left and right_index < len_right:
            if left[left_index] <= right[right_index]:
                sort_array.append(left[left_index])
                left_index += 1
            else:
                sort_array.append(right[right_index])
                right_index += 1
        elif left_index == len_left:
            sort_array.append(right[right_index])
            right_index += 1
        elif right_index == len_right:
            sort_array.append(left[left_index])
            left_index += 1
    if Check(sort_array):
        return sort_array


def merge(array: list) -> list:
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge(array[:middle])
    right = merge(array[middle:])
    return get_merge(left, right)


def quick_sort(array: list) -> list:             #Быстрая сортировка
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