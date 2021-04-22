"""
2.Реализовать класс Person, у которого должно быть два атрибута: age и name.
Также у него должен быть следующий набор методов:
    1.def know(self, another_person_object)
    который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).
    2.def is_known(self, another_person_object)
    который возвращает знакомы ли два человека (True/False)
"""


class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age
        self.__friends = []

    def know(self, other):
        self.__friends.append(other)

    def is_known(self, other):
        return other in self.__friends

    @property
    def friends(self):
        return self.__friends


person1 = Person(28, 'Dima')
person2 = Person(32, 'Vasya')

print(person1.is_known(person2))

person1.know(person2)

print(person1.is_known(person2))
print(person1.friends)