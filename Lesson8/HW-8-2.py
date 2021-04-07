"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""
import random


def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6)


def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6)


def main():
    start = input('Start game yes|no ')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        counter = 10
        while counter:
            player_1_value = first_player()
            player_2_value = second_player()
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(f'First player result in {11-counter} round is {player_1_value}')
            print(f'Second player result in {11 - counter} round is {player_2_value}')

            counter -= 1

        if player_1_sum > player_2_sum:
            print('First player win')
            print(player_1_sum)
            print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print('Draw')
            print(player_1_sum)
            print(player_2_sum)
            return

        print('Second player win')
        print(player_1_sum)
        print(player_2_sum)

main()