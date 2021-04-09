"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""
import random
from datetime import datetime
import csv

first_player_name = input('Enter 1st player name: ')
second_player_name = input('Enter 2nd player name: ')


def first_player():
    input(f'{first_player_name} move ')
    return random.randint(1, 6)


def second_player():
    input(f'{second_player_name} move')
    return random.randint(1, 6)


def main():
    start = input('Start game yes|no: ')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':

        round_num = 1  # for display game round number

        # with open('game.csv', 'w') as csv_game_file:
        #     writer = csv.writer(csv_game_file)
        #     writer.writerow(headers)
        #     for r in range(round_num):
        #         row = ()

        counter = input('How many rounds game do you want play? ')

        if not counter.isdigit():
            raise TypeError('Number of rounds should be a digit')
        counter = int(counter)
        while counter:
            print(f'{round_num} round')
            player_1_value = first_player()
            move_time = datetime.now().strftime("%H:%M:%S")
            print(f'{first_player_name} move time is {move_time}')
            player_2_value = second_player()
            move_time = datetime.now().strftime("%H:%M:%S")
            print(f'{second_player_name} move time is {move_time}')
            if player_1_value == player_2_value:
                print(f'No winner in {round_num} round. Result {player_1_value}: {player_2_value}')
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(f'{first_player_name} result in {round_num} round is {player_1_value}')
            print(f'{second_player_name} result in {round_num} round is {player_2_value}')


            if player_1_value > player_2_value:
                print(f'{first_player_name} won {round_num} round with result: {player_1_value} : {player_2_value}')
            # if player_1_value == player_2_value:
            #     print(f'No winner in {round_num}. Result {player_1_value}: {player_2_value}')
            else:
                print(f'{second_player_name} won {round_num} round with result: {player_2_value} : {player_1_value}')

            print(f'Current total result after {round_num} round is {player_1_sum} : {player_2_sum}')

            counter -= 1
            round_num += 1

        if player_1_sum > player_2_sum:
            print(f'{first_player_name} win game with total result {player_1_sum} : {player_2_sum}')
            # print(player_1_sum)
            # print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print(f'Draw with total result {player_1_sum} : {player_2_sum}')
            # print(player_1_sum)
            # print(player_2_sum)
            return

        print(f'{second_player_name} win game with total result {player_2_sum} : {player_1_sum}')
        # print(player_1_sum)
        # print(player_2_sum)


main()