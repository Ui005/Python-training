"""
Постройть хеш-таблицу из слов произвольного текстового файла, задав ее размерность с экрана.
Вывести построенную таблицу слов на экран. Осуществить поиск введенного слова.
Выполнить программу для различных размерностей таблицы и сравнить количество сравнений.
Удалить все слова, начинающиеся на указанную букву, выведите таблицу.
"""

from prettytable import PrettyTable
# Функция для хэширования
def hash_function(key):
    k = sum(ord(character) for character in repr(key))
    return k

class HashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in set(file)]

    # Добавление элемента в хэш таблицу
    def insert(self, key, value: int):
        hash_key = hash_function(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        bucket.append((key, value))

    # Поиск элемента в таблице
    def retrieve(self, key):
        hash_key = hash_function(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        if len(bucket) == 1:
            if bucket[0][0] == key:
                return bucket[0][1]
        else:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return 0


    def display(self):
        table = PrettyTable()
        table.field_names = ["Буква", "Кол-во в строке"]
        for i in range(len(self.hashmap)):
            for j in range(len(self.hashmap[i])):
                list = dict()
                list["Буква"] = str(hash_function(self.hashmap[i][j][0]))
                list["Кол-во в строке"] = str(self.hashmap[i][j][1])
                table.add_row([list["Буква"], list["Кол-во в строке"]])
        print(table)

    # Удаление элемента из таблицы
    def out(self, key):
        hash_key = hash_function(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        if len(bucket) == 1:
            return self.hashmap.remove(bucket)
        else:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket.pop(i)
                    return self.hashmap
        return "KeyError"


file = open("слова", "r", encoding="utf-8").read().lower().split()
size = int(input("Введите размерность таблицы(если хотите вывести полностью, то введите 0): "))
s = 0
hash_table = HashMap()
for i in set(file):
    if size == 0:
        n = file.count(i)
        hash_table.insert(i, n)
    elif s < size:
        n = file.count(i)
        hash_table.insert(i, n)
        s += 1
    else:
        break
hash_table.display()

element = input("введите слово, которое хотите найти: ").lower()
print("Слово  " + element + "  встречается в файле", hash_table.retrieve(element), "раз(а)")

symbol = input("Слова на какую букву нужно удалить?: ").lower()
a = set([i for i in file if i.startswith(symbol)])
for i in a:
    hash_table.out(i)
hash_table.display()

