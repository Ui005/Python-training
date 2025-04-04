"""
Реализация стека. Элементы меньше 0 заменяем на -1, больше - на 1
"""
class Stack:
    def __init__(self):  #инициализация пустого списка
        self.items = []
    def empty(self):    #проверка пуст ли стек
        return self.items == []

    def addendum(self, item):   #добавление элементов в стек
        self.items.append(item)

    def pop(self):              #извлечение элемента из верхушки стека
        return self.items.pop()

def replacement(stack):
    a = []
    while not stack.empty():    #пока стек не пуст, извлекаем верхний элемент и заменяем его в соот. с условием
        number = stack.pop()
        if number > 0:
            number = 1
        else:
            number = -1
        a.append(number)
    for i in a[::-1]:
        stack.addendum(i)

numbers = list(map(int, input("Введите 10 чисел: ").split()))
stack = Stack()
for num in numbers:
    stack.addendum(num)
replacement(stack)
print("Результат после замен: ",stack.items)