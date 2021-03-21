first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value: ')

try:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
except IndentationError:
    print (f'Value of type {type(value)} {value} is not a digit')
try:
    result = first_value / second_value
except ZeroDivisionError:
    print('Division by 0 not possible')


# if operation == '/':
#     if second_value == 0:
#         print('Division by 0 not possible')
#     elif second_value!=0:
#         print(first_value / second_value)
# elif operation == '+':
#     print(first_value + second_value)
# elif operation == '-':
#     print(first_value - second_value)
# elif operation == '*':
#     print(first_value * second_value)
# elif operation == '//':
#     print(first_value // second_value)
# elif operation == 'sqr':
#     print(first_value * first_value)
# else:
#     print(f'Invalid operation: {operation}')