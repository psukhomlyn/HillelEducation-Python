import json
from pprint import pprint

with open('questions.json') as file:
    file_data = json.load(file)

pprint(file_data, indent=4)

"""
convert dict to json
file_data = json.dumps(file_data)
"""