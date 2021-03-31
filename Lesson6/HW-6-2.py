number: str = input('Please enter a number: ')

if not number.isdigit():
    raise ValueError('Entered value should be an integer')

number: int = int(number)


def even_odd_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(even_odd_number(number))