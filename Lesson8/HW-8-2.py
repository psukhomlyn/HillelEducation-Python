"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""
import random
from datetime import datetime
import json

first_player_name = input('Enter 1st player name: ')
second_player_name = input('Enter 2nd player name: ')


def first_player():
    input(f'{first_player_name} move ')
    return random.randint(1, 6), datetime.now().strftime("%H:%M:%S")


def second_player():
    input(f'{second_player_name} move')
    return random.randint(1, 6), datetime.now().strftime("%H:%M:%S")


def main():
    start = input('Start game yes|no: ')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':

        game_data = {}
        game_total = {}
        game_winner = None

        round_num = 1  # for display game round number

        counter = input('How many rounds game do you want play? ')

        if not counter.isdigit():
            raise TypeError('Number of rounds should be a digit')
        counter = int(counter)
        while counter:
            print(f'{round_num} round')
            player_1_value, first_player_move_time = first_player()
            move_time = datetime.now().strftime("%H:%M:%S")
            print(f'{first_player_name} move time is {move_time}')
            player_2_value, second_player_move_time = second_player()
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
            # round_num += 1

            game_data[f'Round {round_num}'] = {
                'player_1': {
                    'name': first_player_name,
                    'round_sum': player_1_value,
                    'time': first_player_move_time,
                    'current_value' : player_1_sum
                },
                'player_2': {
                    'name': second_player_name,
                    'round_sum': player_2_value,
                    'time': second_player_move_time,
                    'current_value': player_2_sum
                }
            }

            round_num += 1

        with open('game_result.json', 'w') as file:
            json.dump(game_data, file)


        if player_1_sum > player_2_sum:
            print(f'{first_player_name} win game with total result {player_1_sum} : {player_2_sum}')
            game_winner = first_player_name
            # print(player_1_sum)
            # print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print(f'Draw with total result {player_1_sum} : {player_2_sum}')
            game_winner = 'No winner'
            # print(player_1_sum)
            # print(player_2_sum)
            return

        print(f'{second_player_name} win game with total result {player_2_sum} : {player_1_sum}')
        game_winner = second_player_name
        # print(player_1_sum)
        # print(player_2_sum)

        game_total['Game result'] = {
            'game winner': f'{game_winner}',
            'total result': f'{player_1_sum} - {player_2_sum}'
        }

        with open('game_result.json', 'w') as file:
            json.dump(game_total, file)


main()