"""
Original text in test file - The long word in the text. text. Thelongestword in the text.
"""
from collections import Counter

with open('longtext.txt') as test_file:
    file_text = test_file.read()
    print(f'File text is: {file_text}')

words_list: list = file_text.replace('.', ' ').split()  # Split text on words
print(f'The following file has the next words: {words_list}')

most_occured_word = Counter(words_list)
print(f'The most occurred word and occurrence is {most_occured_word.most_common(1)}')

max_length = len(max(words_list, key=len))
for word in words_list:
    if len(word) == max_length:
        print(f'The longest word is "{word}" with length is {max_length} characters')
