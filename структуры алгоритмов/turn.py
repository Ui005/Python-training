"""
Дана очередь символов. Удалить каждый нечетный элемент очереди.
"""
from random import randint
class Queue:
    def __init__(self):
        self.turn = []
    def add(self, value):
        self.turn.append(value)
    def remove(self):
        return self.turn.pop(0)
    def size(self):
        return len(self.turn)
    def empty(self):    #проверка пуста ли очередь
        return self.turn == []

def replacement(queue):
    a = []
    while not queue.empty():    #пока очередь не пуста, извлекаем элементы
        number = queue.remove()
        a.append(number)
    for i in range(1, len(a), 2):
        queue.add(a[i])

n = int(input("введите кол-во элементов в очереди: "))
turn = Queue()
for i in range(n):
    j = randint(-10, 10)
    turn.add(j)
print("Сгенирированная очередь: ", turn.turn)
replacement(turn)
print("Очередь из элементов, стоящих на чётных местах: ", turn.turn)