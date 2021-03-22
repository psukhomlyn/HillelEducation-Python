import random

try:
    random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except ZeroDivisionError:
    print(f'ZeroDivision Error')
except ImportError:
    print(f'Import Error')
except KeyError:
    print(f'Key Error')
except UnicodeError:
    print(f'Unicode Error')
except StopIteration:
    print(f'Stop Iteration Error')
else:
    print(f'Random error covered')


# print(dir(__builtins__))