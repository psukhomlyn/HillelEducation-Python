"""
text in the first_file.txt = 'Hello! This is content of the first file.'
"""

with open('first_file.txt', mode='r+') as first_file:
    first_data = first_file.read()
    print(f'Content of the first file is: {first_data}')

    with open('second_file.txt', mode='w') as second_file:
        second_data = first_data.upper()
        second_file.write(second_data)
        print(f'Content of the second file is: {second_data}')

    first_file.write(' / ' + second_data)

"""
for check that data added to the first file
"""

with open('first_file.txt') as updated_first_file:
    updated_first_data = updated_first_file.read()
    print(f'Content of the first file after update is: {updated_first_data}')