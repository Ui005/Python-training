"""
В текстовом файле содержатся целые числа. Постройть хеш-таблицу для чисел из файла.
Выполнить поиск введенного целого числа в хеш-таблице.
"""
from prettytable import PrettyTable
# Функция для хэширования
def hash_function(key):
    k = sum(ord(character) for character in repr(key))
    return k

class HashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in set(f)]

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



f = open("числа").read().split()
hash_table = HashMap()
for i in set(f):
    n = f.count(i)
    hash_table.insert(i, n)
hash_table.display()


n = input("введите число, которое хотите найти: ")
print("Число  " + n + "  встречается в файле", hash_table.retrieve(n), "раз(а)")

