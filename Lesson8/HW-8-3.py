"""
3. Реализовать функцию, которая принимает строку и разделитель и возвращает словарь {слово: количество повторений}
(частотный словарь)
"""
from collections import Counter


def converter(string, separator):
    words_list = string.split(separator)
    print(words_list)
    freq = Counter(words_list)
    print(freq)
    pass


my_str = input('Enter a string: ')
delimiter = input('Enter a delimiter: ')

print(converter(my_str, delimiter))