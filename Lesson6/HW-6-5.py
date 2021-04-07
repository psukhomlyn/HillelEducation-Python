import json
from pprint import pprint

FILE_CONTENT = None
answers_list = []


def read_file(filename):
    global FILE_CONTENT
    with open(filename) as file:
        FILE_CONTENT = json.load(file)


read_file('questions.json')

questions = FILE_CONTENT['questions']

for element in questions:
    question = element['q']
    answer = input(f'{question} ')
    element['answer'] = answer

FILE_CONTENT['questions'] = questions

"""
Write answers to json
"""


def save_answers(filename):
    global FILE_CONTENT
    with open(filename, 'w') as file:
        json.dump(FILE_CONTENT, file, indent=4)


save_answers('questions.json')

pprint(FILE_CONTENT, indent=4)
