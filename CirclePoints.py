"""
программа находит, сколько точек с целочисленными
координатами попадает в круг радиуса R с центром в точке (x,y).
В начале файла output.txt программа записывает сегодняшнюю дату и
время начала работы программы. В конец файла – время выполнения в
секундах.
"""

from datetime import datetime
import time
def read_file() -> str:
    """чтение из файла"""
    file = open("input.txt").read().strip()
    return file

def data() -> str:
    """с помощью модуля datetime узнаём текущую дату и время"""
    current_date = str(datetime.now())[:10].split("-")
    time_1 = str(datetime.now())[11:16]
    return current_date[2] + "." + current_date[1] + "." + current_date[0] + " " + time_1

def Circle_Points(file: str) -> str:
    """задаём окружность и вычисляем сколько точек с целыми координатами входит в неё"""
    a = []
    c = 0
    for line in file:
        if line != " " and line != "\n":
            a.append(int(line))
    r,x0,y0 = a[0],a[1],a[2]
    for x in range(x0 - r,x0 + r + 1):
        for y in range(y0 - r,y0 + r + 1):
            if (x - x0)**2 + (y - y0)**2 <= r**2:
                c += 1
    return str(c)

def file_write():
    """записываем результат выполнения подпрограмм в файл"""
    start = time.time()
    file = open('output.txt', 'w')
    file.write(str(data()) + "\n" + Circle_Points(read_file()) + "\n")
    end = time.time()
    file.write(str(end - start) + "\n")
    file.close()