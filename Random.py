"""
программу анализирует рабочий каталог на наличие
файла с входными данными input.txt, если файл найден считайте из него число
N и выводит в файл output.txt все простые числа от 1 до N. Если файл не найден
– выведет соответствующее сообщение.
"""

import os
def simple_n(x: int) -> bool:
    """функция проверяет простое ли число"""
    c = 0
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            c += 1
            return False
    if c == 0:
        return True

def Random() -> str:
    """проверка наличия файла в директории и проверка числа до N нан простоту"""
    directory = os.getcwd()
    files = os.listdir(directory)
    if "input.txt" not in files:
        return "Файл с входными данными не обнаружен"
    else:
        a = ""
        N = int(open("input.txt", "r").readline().strip().split()[0])
        for i in range(2, N + 1):
            if simple_n(i):
                a += str(i) + " "
        return a

def write_file():
    f = open("output.txt", "w")
    f.write(Random())
    f.close()