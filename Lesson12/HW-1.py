"""
 Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде уникального набора объектов
 `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades` и тп), а так же необходимый набор методов экземпляра для работы с этими объектами.
    Реализовать функционал, который позволит:
     1. Покинуть студенту группу
     2. Перевестись в другую группу
     3. Покзать средний балл отдельного студента
     4. Показать средний балл по группе
     5. Добавленные по желанию:
     - добавить студента в группу
     - изменить студенту оценку
"""
import uuid
from typing import Optional


class Student:
    def __init__(self, name: str, age: int, grades: Optional[dict], group: 'Group'):
        self.name = name
        self.age = age
        self.grades = grades or {}
        self.group = group
        self._id = uuid.uuid4()

    def leave_group(self):
        self.group.delete_student(self)

    def change_group(self, other_group):
        self.group.delete_student(self)
        other_group.add_student(self)

    def add_group(self):
        self.group.add_student(self)

    @property
    def avg_rate(self):
        return sum(self.grades.values()) / len(self.grades)

    # def change_grade(self):
    #     self.grades = self.grades.update["math"]


class Group:
    def __init__(self, name: str):
        self.name = name
        self.students = {}

    @property
    def avg_rate(self):
        return sum([student.avg_rate for student in self.students.values()]) / len(self.students)

    def add_student(self, student):
        self.students.setdefault(student._id, student)
        student.group = self

    def delete_student(self, student: Student):
        self.students.pop(student._id, None)
        student.group = None


def code_check():
    first_group = Group(name='1st Group')
    second_group = Group(name='2nd Group')
    oleg = Student(name='Oleg', age=21, grades={'math': 5, 'bio': 4, 'history': 5}, group=first_group)
    viktor = Student(name='Viktor', age=23, grades={'math': 5, 'bio': 3, 'history': 3}, group=first_group)
    # oleg.change_grade()
    # print(oleg.name, oleg.grades)
    print(oleg.name, oleg.group, oleg.avg_rate)  # принт студента 1
    print(viktor.name, viktor.group, viktor.avg_rate)  # принт студента 2
    first_group.add_student(oleg)  # добавление студента 1 в группу 1
    print(first_group.students, first_group.avg_rate)  # оценки студента и группы равны
    first_group.add_student(viktor)  # добавление студента 2 в группу 1
    print(first_group.students, first_group.avg_rate)  # оценка группы изменилась
    oleg.change_group(second_group) # студент 1 перешел в группу 2
    print(oleg.name, oleg.group.name, oleg.avg_rate)
    print(second_group.students, second_group.avg_rate)
    print(first_group.students, first_group.avg_rate)
    print(viktor.name, viktor.group.name)

code_check()