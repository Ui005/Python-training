"""Создание структуры с полями"""
class Discipline:         #
    def __init__(self, cod_discipline: int, name_discipline: str, surname: str, cod_group: str,
                 number_of_students: int, lecture_hours: int, practice_hours: int, result_control: int, start_data: str, next_item=None):
        self.cod_discipline = cod_discipline
        self.name_discipline = name_discipline
        self.surname = surname
        self.cod_group =cod_group
        self.number_of_students =number_of_students
        self.lecture_hours = lecture_hours
        self.practice_hours =practice_hours
        self.result_control = result_control
        self.start_data = start_data
        self.next_item = next_item

    def __str__(self): #метод для преобразования одной записи списка в строку для вывода
        return (f"КОД ДИСЦИПЛИНЫ: {self.cod_discipline}, Название: {self.name_discipline}, Фамилия преподавателя: {self.surname}" + "\n" +
               f" Код группы: {self.cod_group}, Число студентов: {self.number_of_students}, Часы лекций: {self.lecture_hours} " + "\n" +
                f"Часы практик: {self.practice_hours}, итоговый контроль: {self.result_control}, Дата начала курса: {self.start_data}" + "\n")

class DisciplineLinkedList: #создаем связный список
    def __init__(self):
        self.head = None #ссылка на первый элемент списка. Сейчас он пуст

    def append(self, cod_discipline: int, name_discipline: str, surname: str, cod_group: str,
                 number_of_students: int, lecture_hours: int, practice_hours: int, result_control: int, start_data: str):
        if not self.head:
            self.head = Discipline(cod_discipline, name_discipline, surname, cod_group,
                 number_of_students, lecture_hours, practice_hours, result_control, start_data)
        else:
            current = self.head
            while current.next_item:
                current = current.next_item
            current.next_item = Discipline(cod_discipline, name_discipline, surname, cod_group,
                 number_of_students, lecture_hours, practice_hours, result_control, start_data)

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(f"{current}")
            current = current.next_item
        return "\n".join(items)

    def sort_by_surname(self):
        #Преобразование в обычный список
        unsorted_list = []
        current = self.head
        while current:
            unsorted_list.append(current)
            current = current.next_item

            #Сортировка списка
        sorted_list = sorted(unsorted_list, key=lambda x: x.surname)

        #Перестроение связного списка
        self.head = None
        for x in sorted_list:
            self.append(x.cod_discipline, x.name_discipline, x.surname, x.cod_group,
                 x.number_of_students, x.lecture_hours, x.practice_hours, x.result_control, x.start_data)

    def sort_by_hours(self):
        unsorted_list = []
        current = self.head
        while current:
            unsorted_list.append(current)
            current = current.next_item

        sorted_list = sorted(unsorted_list, key=lambda item: item.lecture_hours + item.practice_hours)

        self.head = None
        for x in sorted_list:
            self.append(x.cod_discipline, x.name_discipline, x.surname, x.cod_group,
                 x.number_of_students, x.lecture_hours, x.practice_hours, x.result_control, x.start_data)

    def sort_by_date(self):
        unsorted_list = []
        current = self.head
        while current:
            unsorted_list.append(current)
            current = current.next_item

        sorted_list = sorted(unsorted_list, key=lambda item: item.start_data)

        self.head = None
        for x in sorted_list:
            self.append(x.cod_discipline, x.name_discipline, x.surname, x.cod_group,
                 x.number_of_students, x.lecture_hours, x.practice_hours, x.result_control, x.start_data)

    def find_by_surname(self, surname: str):
        current = self.head #начинаем поиск с начала (head)
        while current:#продолжаем, пока есть элементы
            if current.surname == surname:
                return f"{current}" #возвращаем нужный элемент
            current = current.next_item
        return "Элемент не найден" #в противном случае

    def find_by_hours(self, hours: int):
        current = self.head
        while current:
            if current.lecture_hours + current.practice_hours == hours:
                return f"{current}"
            current = current.next_item
        return "Элемент не найден"

    def find_by_date(self, start_data: str):
        current = self.head
        while current:
            if current.start_data == start_data:
                return f"{current}"
            current = current.next_item
        return "Элемент не найден"

#Список заполняется значениями
"""Данные о дисциплинах"""
discipline = DisciplineLinkedList()

discipline.append(16, "Архитектура ЭВМ", "Алеева", "КЭ - 141",
                         28, 16, 8, "Зачёт", "05.02.2024")
discipline.append(10, "Дискретная математика", "Макаровских", "КЭ - 142",
                         23, 32, 30, "Экзамен", "01.09.2023")
discipline.append(5, "История России", "Волков", "КЭ - 143",
                         20, 14, 6, "Зачёт", "01.09.2021")

#С помощью ввода с клавиатуры выбираем действие и выводим результат на экран
choice1 = str(input('Введите действие (Отсортировать/найти): '))
if (choice1 == 'Отсортировать') or (choice1 == 'отсортировать'):
    choice2 = str(input("Введите, по какому значению хотите отсортировать? (Кол-во часов/дата/Фамилия преподавателя): "))
    if (choice2 == 'Фамилия преподавателя') or (choice2 == 'фамилия преподавателя'):
        discipline.sort_by_surname()
        print(discipline.display())
    if (choice2 == 'Дата') or (choice2 == 'дата'):
        discipline.sort_by_date()
        print(discipline.display())
    if (choice2 == 'Кол-во часов') or (choice2 == 'кол-во часов'):
        discipline.sort_by_hours()
        print(discipline.display())

elif (choice1 == 'Найти') or (choice1 == 'найти'):
    choice2 = str(input("Введите, по какому значению хотите найти? (Кол-во часов/дата/Фамилия преподавателя): "))
    if (choice2 == 'Фамилия преподавателя') or (choice2 == 'фамилия преподавателя'):
        choice3 = str(input('Введите артикул: '))
        print(discipline.find_by_surname(choice3))
    if (choice2 == 'Дата') or (choice2 == 'дата'):
        choice3 = str(input('Введите дату: '))
        print(discipline.find_by_date(choice3))
    if (choice2 == 'Кол-во часов') or (choice2 == 'кол-во часов'):
        choice3 = int(input('Введите количество: '))
        print(discipline.find_by_hours(choice3))

