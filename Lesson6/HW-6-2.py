digit = input('Please enter a digit: ')
digit = int(digit)

def even_odd_number():
    if digit % 2 == 0:
        return True
    else:
        return False

print(even_odd_number())