import sys
import string

email: str = input('Input email: ')
password: str = input('Enter password: ')

is_digit_found = False
is_symbol_found = False

# Email validation
if '@' not in email:
    raise NameError('Email should include @')
    # print('Invalid email')
    # sys.exit(0)
elif '.' not in email:
    raise NameError('Email domain should include a dot')
    # print('Invalid email')
    # sys.exit(0)
at_sign_index = email.index('@')
for sign in {'.', '@'}:
    if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
        raise NameError('Invalid email.')
        # print('Invalid email')
        # sys.exit(0)
    elif email[-1] == sign or email[0] == sign:
        raise NameError('Invalid email.')
        # print('Invalid')
        # sys.exit(0)

# Password validation

if len(password) < 8:
    raise NameError('Invalid password. Password should be at least 8 characters.')
if ' ' in password:
    raise NameError('Invalid password. Password cannot include spaces.')

for char in password:
    if char in string.digits:
        is_digit_found = True
    elif char in {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')'}:
        is_symbol_found = True
    if is_digit_found and is_symbol_found:
        print('Password is valid')
        break

if not is_digit_found:
    raise NameError(f'Invalid password. Password should include a digit.')
if not is_symbol_found:
    raise NameError(f'Invalid password. Password should include a symbol.')