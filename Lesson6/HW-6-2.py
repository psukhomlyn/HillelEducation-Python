number: str = input('Please enter a number: ')


if not number.isdigit():
    raise ValueError('Entered value should be a number')

number: int = int(number)

def even_odd_number():
    if number % 2 == 0:
        return True
    else:
        return False

print(even_odd_number())