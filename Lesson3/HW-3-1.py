first_value_str: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value_str: str = input('Input second value: ')
# result: float

try:
    first_value_int: int = int(first_value_str)
    second_value_int: int = int(second_value_str)
except ValueError:
    print(f'Both values should be a digits')
else:
    if operation == '+':
        result = first_value_int + second_value_int
    elif operation == '-':
        result = first_value_int - second_value_int
    elif operation == '*':
        result = first_value_int * second_value_int
    elif operation == '/':
        try:
            result = first_value_int / second_value_int
        except ZeroDivisionError:
            print('Division by 0 not possible')
    elif operation == '//':
        try:
            result = first_value_int // second_value_int
        except ZeroDivisionError:
            print('Division by 0 not possible')
    elif operation == '**':
        result =  first_value_int * first_value_int
    else:
        print(f'Invalid operation: {operation}')
try:
    print(result)
except NameError:
    print(f'Not possible to get result')