num = input('Please enter a number: ')

if not num.isdigit():
    raise ValueError('Entered value should be an integer')

num: int = int(num)


def is_prime(x):
    if x <= 1 or x % 1 > 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# print(is_prime(num))
if is_prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')