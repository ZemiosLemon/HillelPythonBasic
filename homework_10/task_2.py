mail = input()


def hide_email(email: str) -> str:
    first_part, second_part = email.split('@')
    return f'{first_part[:-3]}***@**{second_part[2:]}'


print(hide_email(mail))