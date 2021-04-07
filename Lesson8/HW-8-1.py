num1 = input('Please input the first number: ')
if not num1.isdigit():
    raise TypeError (f' First value should be a digit')

num2 = input('Please input the second number: ')
if not num2.isdigit():
    raise TypeError (f' Second value should be a digit')

num3 = input('Please input the third number: ')
if not num3.isdigit():
    raise TypeError (f' Third value should be a digit')

origin_list = [num1, num2, num3]
# print(origin_list)

origin_num = ''.join(origin_list)


def Max_num(inum):
    count = [0 for x in range(10)]
    string = str(origin_num)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1

    result = 0
    multiplier = 1

    for j in range(10):
        while count[j] > 0:
            result = result + (j * multiplier)
            count[j] = count[j] - 1
            multiplier = multiplier * 10

    return result


print(Max_num(origin_num))