import json
from pprint import pprint

FILE_CONTENT = None
answer1 = input('What is your name? ')
answer2 = input('How old are you? ')
answer3 = input('Do you like python? ')
answer4 = input('What is the most difficult topic for you? ')
answer5 = input('Please write suggestions and wishes ')


def read_file(filename):
    global FILE_CONTENT
    with open(filename) as file:
        FILE_CONTENT = json.load(file)


read_file('questions.json')
pprint(FILE_CONTENT, indent=4)
print(type(FILE_CONTENT))

# value = FILE_CONTENT['questions']
# print(value)
# print(type(value))


def put_answers():
    global FILE_CONTENT
    FILE_CONTENT['questions'][0]['answer'] = answer1
    FILE_CONTENT['questions'][1]['answer'] = answer2
    FILE_CONTENT['questions'][2]['answer'] = answer3
    FILE_CONTENT['questions'][3]['answer'] = answer4
    FILE_CONTENT['questions'][4]['answer'] = answer5


put_answers()
pprint(FILE_CONTENT, indent=4)


# def save_answers(filename):
#     global FILE_CONTENT
#     with open(filename, 'w') as file:
#         json.dump(FILE_CONTENT, file, indent=4
#
#
# save_answers('questions.json')
