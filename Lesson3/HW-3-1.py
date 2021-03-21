first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
except ValueError:
    print (f'Both values should be a digits')
else:
    if operation == '+':
        print(first_value + second_value)
    elif operation == '-':
        print(first_value - second_value)
    elif operation == '*':
        print(first_value * second_value)
    elif operation == '/':
        try:
            result1 = first_value / second_value
        except ZeroDivisionError:
            print('Division by 0 not possible')
        else:
            print(result1)
    elif operation == '//':
        try:
            result2 = first_value // second_value
        except ZeroDivisionError:
            print('Division by 0 not possible')
        else:
            print(result2)
    elif operation == '**':
        print(first_value * first_value)
    else:
        print(f'Invalid operation: {operation}')