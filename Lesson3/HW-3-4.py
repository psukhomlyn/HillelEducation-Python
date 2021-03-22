# Task 4

first_value_str: str = input('Input first value: ')
second_value_str: str = input('Input second value: ')

my_list: list = []

try:
    first_value_int: int = int(first_value_str)
    second_value_int: int = int(second_value_str)
except ValueError:
    print(f'Both values should be a digits')
if second_value_int <= first_value_int:
    raise NameError(f'Second value should be bigger then the first value')
else:
    for item in range(first_value_int, second_value_int):
        if item % 5 == 0:
            my_list.append(item)
    print(f'Your list is {my_list}')

# Task 5
total_value = 0

for i in my_list:
    total_value = total_value + i

print(f'Min value is {min(my_list)}')
print(f'Max value is {max(my_list)}')
print(f'Total value is {total_value}')