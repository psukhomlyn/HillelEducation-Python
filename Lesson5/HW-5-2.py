numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

"""
1st way - for print digits as list of digits
"""
digits = []

for digit in numbers:
    if digit % 2 == 0:
        digits.append(digit)
    elif digit == 237:
        break
print(f'List of digits is: {digits}')

"""
2nd way - for print digits as a just digits
"""
for digit in numbers:
    if digit % 2 == 0:
        print(digit)
    elif digit == 237:
        break
