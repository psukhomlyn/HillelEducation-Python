import json
from pprint import pprint

FILE_CONTENT = None
answers_list = []

def read_file(filename):
    global FILE_CONTENT
    with open(filename) as file:
        FILE_CONTENT = json.load(file)


read_file('questions.json')
# pprint(FILE_CONTENT, indent=4)
# print(type(FILE_CONTENT))

questions = FILE_CONTENT['questions']  #json dict value
# print(questions)
# print(type(questions))
#
# print(questions[0])
# print(type(questions[0]))


# question = questions[0]['q']

for q_element in questions:
    question = q_element['q']
    answer = input(f'{question} ')
    answers_list.append(answer)
# print(answers_list)

"""
Put answers to json
"""
def put_answers():
    global FILE_CONTENT
    for a_element in answers_list:
        print(a_element, type(a_element))
        FILE_CONTENT['questions'][a_element]['answer'] = answers_list[a_element]

put_answers()
pprint(FILE_CONTENT, indent=4)

"""
Write answers to json
"""
# def save_answers(filename):
#     global FILE_CONTENT
#     with open(filename, 'w') as file:
#         json.dump(FILE_CONTENT, file, indent=4
#
#
# save_answers('questions.json')
