"""
программа, которая получает список файлов в текущей
директории,определяет присутствует ли в директории файл input.txt. Если файл input.txt
имеется в текущей директории, то программа должна считать из файла
input.txt число и выводит в файл output.txt:
 само число,
 количество цифр в числе,
 сумму цифр в числе,
 произведение цифр в числе.
Если файл input.txt не обнаружен в рабочем каталоге – программа
выдаёт соответствующее сообщение.
"""

import os
def SearchFile() -> str:
    """проверка наличия файла в директории и нахождение нужной информации о числе в файле"""
    directory = os.getcwd()
    files = os.listdir(directory)
    if "input.txt" not in files:
        return ("Файл с входными данными не обнаружен")
    else:
        number = open("input.txt", "r").readline().strip().split()[0]
        len_n = str(len(number))
        a = list(map(int, [x for x in number]))
        sum_n = str(sum(a))
        p = 1
        for i in range(len(a)):
            p *= a[i]
    return "Число:" + number + "\n" + "Количество цифр:" + len_n + "\n" + "Cумма цифр:" + sum_n + "\n" + "Произведение цифр:" + str(p) + "\n"


def file_write():
    """запись результата в файл"""
    f = open("output.txt", "w")
    f.write(SearchFile())
    f.close()