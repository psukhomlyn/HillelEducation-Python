"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, сменить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
Следует учесть:
 - у воина может быть броня
 - здоровье не может быть меньше 0
 - броня не может быть меньше 0
 - здоровье не тратится пока броня не 0
Было бы неплохо добавить возможность воину носить несколько видов оружия и при сломаном текущем заменить его (опционально)
"""
from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = randint(1, 101)
        self.status = 'alive'

    def add_health(self, value):
        if value < 0:
            print('Слишком мало')
            return
        self.health += value

    def change_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        if armor < 0:
            print('Слишком мало')
            return
        self.armor += armor

    def heat_other(self, other_warrior):
        if other_warrior.status == 'die':
            print(other_warrior.name + ' is die')
            raise Exception
        if other_warrior.armor:
            predict = other_warrior.armor - self.weapon.power
            if predict < 0:
                other_warrior.armor -= self.weapon.power + predict
                other_warrior.health += predict
                return
            other_warrior.armor -= self.weapon.power
            return
        predict = other_warrior.health - self.weapon.power
        if predict < 0:
            other_warrior.status = 'die'
            return
        other_warrior.health -= self.weapon.power


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 101)
        ))
    return choice(weapon_list)


def fight():
    samurai = Warrior(name='Hikaru', health=100, weapon=random_choose_weapon())
    viking = Warrior(name='Olof', health=100, weapon=random_choose_weapon())
    while True:
        print(f'Samurai {samurai.name} has: heath - {samurai.health}, weapon power - {samurai.weapon.power}, armor - {samurai.armor}')
        print(f'Viking {viking.name} has: heath - {viking.health}, weapon power - {viking.weapon.power}, armor - {viking.armor}')
        samurai.heat_other(viking)
        print(f'Samurai damage {samurai.weapon.power}')
        print(f'After samuray {samurai.name} beat viking {viking.name}')
        print(f'Samurai {samurai.name} has: heath - {samurai.health}, weapon power - {samurai.weapon.power}, armor - {samurai.armor}')
        print(f'Viking {viking.name} has: heath - {viking.health}, weapon power - {viking.weapon.power}, armor - {viking.armor}')
        viking.heat_other(samurai)
        print(f'Viking damage {viking.weapon.power}')
        print(f'After viking {viking.name} beat samuray {samurai.name}')
        # print(f'Samuray {samuray.name} has: heath - {samuray.health}, weapon power - {samuray.weapon.power}, armor - {samuray.armor}')
        # print(f'Viking {viking.name} has: heath - {viking.health}, weapon power - {viking.weapon.power}, armor - {viking.armor}')


fight()