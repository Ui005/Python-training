"""
Алгоритм упорядоченного дерева поиска. Находит ключ поиска и удаляет его из дерева.
"""
import random
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root

# Запрашиваем у пользователя размер массива и ключ поиска
size = int(input("Введите размер массива: "))
search_key = int(input("Введите ключ поиска: "))

# Формируем массив случайных чисел
array = [random.randint(1, 5) for i in range(size)]

# Создаем корень дерева
root = None
for key in array:
    root = insert(root, key)

print("Исходное дерево:")
inorder(root)

# Ищем и удаляем ключ поиска из дерева
search_result = search(root, search_key)
if search_result:
    print("\nКлюч найден в дереве")
    root = deleteNode(root, search_key)
    print("Дерево после удаления ключа:")
    inorder(root)
else:
    print("\nКлюч не найден в дереве")










