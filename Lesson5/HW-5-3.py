with open('longtext.txt') as test_file:
    file_text = test_file.read()
    print(f'File text is: {file_text}')

words = file_text.split()

max_length = len(max(words, key=len))
for word in words:
    if len(word) == max_length:
        print(f'The longest word is "{word}" and his length is {max_length}')