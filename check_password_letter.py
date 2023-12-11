# Password checker program
input_password = input('Enter your password: ')

digit_checker = False
upper_checker = False
lower_checker = False
len_cheker = False

for ch in input_password:
    if ch.isdigit():
        digit_checker = True

    elif ch.isupper():
        upper_checker = True

    elif ch.islower():
        lower_checker = True

if len(input_password) >= 8:
    len_cheker = True

if not len_cheker:
    print('Password has to be at least 8 characters long.')

if not digit_checker:
    print('Password has to have at least one digit.')

if not lower_checker:
    print('Password has to have at least one lowercase letter.')

if not upper_checker:
    print('Password has to have at least one uppercase letter.')

if len_cheker and digit_checker and lower_checker and upper_checker:
    print('Password is OK.')