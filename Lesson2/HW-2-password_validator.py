"""
password validation rules:
1. password should be 8 characters or more
2. password cannot contain spaces
3. password should include at least 1 digit and 1 special symbol (Shift+digit on keyboard)
"""

password: str = input('Enter password: ')

is_digit_found = False
is_symbol_found=False

if len(password) < 8:
    print('Invalid password. Password should be at least 8 characters.')
elif ' ' in password:
    print('Invalid password. Password cannot include spaces.')
else:
    for char in password:
        if char in {'1','2','3','4','5','6','7','8','9','0'}:
            is_digit_found = True
        elif char in {'!','@','#','$','%','^','&','*','(',')'}:
            is_symbol_found = True
        if is_digit_found is True and is_symbol_found is True:
            break
    if is_digit_found is False:
        print('Invalid password. Password should include a digit.')
    if is_symbol_found is False:
        print('Invalid password. Password should include a symbol.')

