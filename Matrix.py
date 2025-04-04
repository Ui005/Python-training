"""
Программно генерирует случайную прямоугольную матрицу A
размера NхM (N и M считываются из файла input.txt) и прямоугольную матрицу B размера MхK (K –
случайное число из диапазона 5..15). Выводит матрицы A и В в
файл. Делит элементы каждой строки в матрице А на наибольший элемент этой строки,
умножает получившуюся матрицу на матрицу В и выводит результат в файл.
"""

import random

def Matrix_made_(a: int, b: int, n: int) -> list: #a - кол-во строк в матрице,b - кол-во столбцов,n - max элемент матрицы
    """создание матрицы"""
    matrix = []
    for i in range(a):
        matrix.append([])
        for j in range(b):
            matrix[i].append(random.randint(0, n))
    return matrix

def Matrix_made_2(matrix: list) -> list:
    """деление каждого элемента строк матрицы на max элемент этой строки"""
    matrix_1 = []
    for i in range(len(matrix)):
        matrix_1.append(list(map(lambda x: x / max(matrix[i]), matrix[i])))
    return matrix_1

def Matrix_p(matrix1: list, matrix2: list) -> list:
    """произведение матриц"""
    matrix_C = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for k in range(len(matrix2[0])):
            for j in range(len(matrix2)):
                matrix_C[i][k] += matrix1[i][j] * matrix2[j][k]
            matrix_C[i][k] = round(matrix_C[i][k], 2)
    return matrix_C

def read_file() -> [int, int, int]:
    """чтение данных из файла"""
    f = open("input.txt").read()
    N = int(f[0])                    # кол-во строк в матрице А
    M = int(f[2])                    # кол-во столбцов в матрице А и кол-во строк в матрице В
    K = random.randint(5, 16)  # кол-во столбцов в матрице В
    return N, M, K


def file_write():
    N, M, K = read_file()
    matrix_A = Matrix_made_(N,M,50)
    matrix_B = Matrix_made_(M,K,50)
    matrix_C = Matrix_p(Matrix_made_2(matrix_A), matrix_B)
    file = open("output.txt", "w")
    file.write("Матрица А:" + "\n")
    for i in range(N):
        file.write(str(matrix_A[i]) + "\n")
    file.write("Матрица B:" + "\n")
    for i in range(M):
        file.write(str(matrix_B[i]) + "\n")
    file.write("Матрица A*B:" + "\n")
    for i in range(N):
        file.write(str(matrix_C[i]) + "\n")
    file.close()
