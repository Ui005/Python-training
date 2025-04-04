"""
Журнал БРС
Структура данных для хранения баллов для нескольких студентов по любой дисциплине. В первом столбце хранятся ФИО студентов,
в остальных столбцах (>4) хранятся оценки за выполненные контрольно-рейтинговые мероприятия или КРМ.
Пусть максимальный балл за каждое КРМ - 4. А вес КРМ равен порядковому номеру КРМ в семестре.
Задача:
Заполнить таблицу данными о студентах (>5 записей): добавить ФИО.
Организовать заполнение баллов по КРМ случайным образом . Например, если n-случайное число:
n in [0,5) => 0 баллов
n in [5,10) => 1 балл
n in [10,20) => 2 балла
n in [20,30) => 3 балла
n in [30,35) => 4 балла
Для каждого столбца КРМ добавить столбец "Рейтинг i КРМ", содержащий рейтинг студента по i-ому КРМ.
Добавить столбец «Рейтинг текущего контроля». Заполнить его значениями, используя формулу.
Добавить столбец "Оценка за дисциплину" и заполнитб соответствующими значениями по шкале БРС
"""

import random
from prettytable import PrettyTable
def scores_crm() -> list:
    """заполнение баллов по КРМ случайным образом"""
    scores = []
    for k in range(0, 5):
        n = random.randint(0, 35)
        if 0 <= n < 5:
            scores.append(0)
        if 5 <= n < 10:
            scores.append(1)
        if 10 <= n < 20:
            scores.append(2)
        if 20 <= n < 30:
            scores.append(3)
        if 30 <= n <= 35:
            scores.append(4)
    return scores

def rating_crm(scores: list) -> list:
    """подсчёт рейтинга студента по i-ому КРМ в %"""
    rating_student = []
    for i in range(len(scores)):
        percent = scores[i] / 4 * 100
        rating_student.append(percent)
    return rating_student

def Current_control_rating(rating_student: list) -> float:
    """подсчёт Рейтинга текущего контроля» студента"""
    summ, summ_weight = 0, sum([i for i in range(0, len(rating_student) + 1)])
    for i in range(len(rating)):
        summ += (i + 1) * rating[i]
    current_rating_student = summ / summ_weight
    return current_rating_student

def Intermediate_certification_rating() -> int:
    """Рейтинг промежуточной аттестации(случайное число)"""
    n = random.randint(0, 100)
    return n

def Rating_by_discipline(current_rating: float, n: int) -> float:
    """подсчёт Рейтинга по дисциплине"""
    rd = max(0.6 * current_rating + 0.4 * n, current_rating)
    return rd

def Assessment_for_discipline(rd: float) -> str:
    """определение оценки ро дисциплине"""
    assessment_student = ''
    if rd < 60:
        assessment_student = 'Неудовлетворительно'
    if 60 <= rd <= 74:
        assessment_student = 'Зачтено(Удовлетворительно)'
    if 75 <= rd <= 84:
        assessment_student = 'Зачтено(Хорошо)'
    if 85 <= rd <= 100:
        assessment_student = 'Зачтено(Отлично)'
    return assessment_student


table1 = PrettyTable()
table1.field_names = ["№", "ФИО Студента", "Рейтинг текущего контроля", "Рейтинг промежуточной аттестации", "Рейтинг по дисциплине",
                      "Оценка по дисциплине"]

table2 = PrettyTable()
table2.field_names = ["№", "ФИО Студента", "КРМ 1", "Рейтинг 1 КРМ(%)", "КРМ 2", "Рейтинг 2 КРМ(%)", "КРМ 3", "Рейтинг 3 КРМ(%)","КРМ 4",
                      "Рейтинг 4 КРМ(%)", "КРМ 5", "Рейтинг 5 КРМ(%)", "Рейтинг текущего контроля"]

N = int(input("Введите кол-во учеников: "))

for i in range(N):
    """заполнение таблицы"""
    CRM = scores_crm()
    rating = rating_crm(CRM)
    current_rating = Current_control_rating(rating)
    intermediate_rating = Intermediate_certification_rating()
    Rd = Rating_by_discipline(current_rating, intermediate_rating)
    assessment = Assessment_for_discipline(Rd)

    list1 = dict()
    list1["ФИО Студента"] = input("Введите ФИО студента: ")
    list1["Рейтинг текущего контроля"] = current_rating
    list1["Рейтинг промежуточной аттестации"] = intermediate_rating
    list1["Рейтинг по дисциплине"] = Rd
    list1["Оценка по дисциплине"] = assessment
    list1["№"] = i + 1
    table1.add_row(
        [list1["№"], list1["ФИО Студента"], list1["Рейтинг текущего контроля"], list1["Рейтинг промежуточной аттестации"],
         list1["Рейтинг по дисциплине"], list1["Оценка по дисциплине"]])

    list2 = dict()
    for j in range(0, 5):
        list2["КРМ %d" % (j + 1)] = CRM[j]
        list2["Рейтинг %d КРМ(%%)" % (j + 1)] = rating[j]
    list2["Рейтинг текущего контроля"] = current_rating
    table2.add_row(
        [list1["№"], list1["ФИО Студента"], list2["КРМ 1"], list2["Рейтинг 1 КРМ(%)"], list2["КРМ 2"], list2["Рейтинг 2 КРМ(%)"], list2["КРМ 3"],
         list2["Рейтинг 3 КРМ(%)"], list2["КРМ 4"], list2["Рейтинг 4 КРМ(%)"], list2["КРМ 5"], list2["Рейтинг 5 КРМ(%)"],
         list2["Рейтинг текущего контроля"]])

Number_student = int(input("Введите порядковый номер студента, чьи данные вы хотите вывести отдельно: "))

print(table2[Number_student - 1])
print(table1)







