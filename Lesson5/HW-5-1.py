from pathlib import Path

file = input('Please enter a file path OR file name: ')

if "." not in file:
    raise NameError(f'File cannot be without extension')

ext = Path(file).suffix
print(f'File extension is {ext}')