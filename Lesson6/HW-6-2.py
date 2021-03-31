number: str = input('Please enter a number: ')

if not number.isdigit():
    raise ValueError('Entered value should be an integer')

number: int = int(number)


def even_odd_number(num):
    return num % 2 == 0


if even_odd_number(number):
    print(f'Number {number} is even')
else:
    print(f'Number {number} is odd')