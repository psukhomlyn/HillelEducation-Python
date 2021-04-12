"""
3. Реализовать функцию, которая принимает строку и разделитель и возвращает словарь {слово: количество повторений}
(частотный словарь)
"""
from collections import Counter

my_str = input('Enter a string: ')
delimiter = input('Enter a delimiter: ')


def converter(string, separator):
    words_list = string.split(separator)
    print(words_list)
    freq = Counter(words_list)
    return freq


print(converter(my_str, delimiter))