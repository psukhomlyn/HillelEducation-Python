str = input('Please enter a string: ')


def string_transform(item):
    transform_value = 0
    transform_list = []
    for char in (item):
        if char == 'i':
            transform_value += 1
        elif char == 'd':
            transform_value -= 1
        elif char == 's':
            transform_value *= transform_value
        elif char == 'o':
            transform_list.append(transform_value)
    return transform_list


print(string_transform(str))