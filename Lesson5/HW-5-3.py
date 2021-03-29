"""
Original text in test file - The long word in the text. Thelongestword in the text. text.
"""

count = 0

with open('longtext.txt') as test_file:
    file_text = test_file.read()
    print(f'File text is: {file_text}')

words = file_text.replace('.',' ').split()  # Split text on words

for w in range(0, len(words)):
    # count == 1;
    for v in range(w+1, len(words)):
        if words[w] == words[v]:
            count = count + 1

print(f'The most occurred word is: "{words[w]}" and it occurred {count} times.')

max_length = len(max(words, key=len))
for word in words:
    if len(word) == max_length:
        print(f'The longest word is "{word}" with length is {max_length} characters')