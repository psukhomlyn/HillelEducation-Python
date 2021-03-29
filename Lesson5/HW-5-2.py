numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
# digits = []   # 1st way - for print digits as list of digits
#
# for digit in numbers:
#     if digit % 2 == 0:
#         digits.append(digit)
#     elif digit == 237:
#         break
# print(f'List of digits is: {digits}')

for digit in numbers:  # 2nd way - for print digits as a just digits
    if digit % 2 == 0:
        print(digit)
    elif digit == 237:
        break
