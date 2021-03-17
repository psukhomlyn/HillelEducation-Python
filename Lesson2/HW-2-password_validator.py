"""
password validation rules:
1. password should be 8 characters or more
2. password cannot contain spaces
3. password should include at least 1 digit and 1 special symbol (Shift+digit on keyboard)
"""
import string

password: str = input('Enter password: ')

is_digit_found = False
is_symbol_found = False

if len(password) < 8:
    print('Invalid password. Password should be at least 8 characters.')
elif ' ' in password:
    print('Invalid password. Password cannot include spaces.')
else:
    for char in password:
        if char in string.digits:
            is_digit_found = True
        elif char in {'!','@','#','$','%','^','&','*','(',')'}:
            is_symbol_found = True
        if is_digit_found and is_symbol_found:
            print('Password is valid')
            break
    if not is_digit_found:
        print('Invalid password. Password should include a digit.')
    if not is_symbol_found:
        print('Invalid password. Password should include a symbol.')

