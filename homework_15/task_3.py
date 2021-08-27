import re


def check_pass(pass_input):
    if not re.search(r'[a-z]', pass_input):
        return 'Как минимум 1 символ от a-z'
    if not re.search('[A-Z]', pass_input):
        return 'Как минимум 1 символ от A-Z'
    if not re.search('[0-9]', pass_input):
        return 'Как минимум 1 символ от 0-9'
    if not re.search('[$#@+=-]', pass_input):
        return 'Как минимум 1 символ из $#@-+= '
    if len(pass_input) < 8:
        return 'Минимальная длина пароля 8 символов'
    return 'Password is correct'


def user_input():
    password_input = input()
    print(check_pass(password_input))


user_input()

