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

    def change_grade(self):
        self.grades = self.grades.update[science]


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


def chek_its_ok():
    new_group = Group(name='new_group')
    other_group = Group(name='other_group')
    oleg = Student(name='Oleg', age=21, grades={'math': 4, 'bio': 4, 'history': 5}, group=new_group)
    andrey = Student(name='Andrey', age=22, grades={'math': 5, 'bio': 3, 'history': 5}, group=new_group)
    print(oleg.name, oleg._id, oleg.avg_rate)
    print(andrey.name, andrey._id, andrey.avg_rate)
    new_group.add_student(andrey)
    new_group.add_student(oleg)
    new_group.add_student(oleg)
    print(new_group.students)
    print(new_group.avg_rate)
    print(oleg.name, oleg.group.name)
    print(andrey.name, andrey.group.name)
    oleg.change_group(other_group)
    print(oleg.name, oleg.group.name)
    print(other_group.students)
    print(new_group.students)
    print(andrey.name, andrey.group.name)
    new_group.delete_student(andrey)
    print(new_group.students)
    # print(andrey.name, andrey.group.name)
    new_group.delete_student(oleg)


chek_its_ok()