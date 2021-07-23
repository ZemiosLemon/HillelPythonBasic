mail = input()


def hide_email(email: str) -> str:
    split_email = email.split('@')
    return f'{split_email[0][0:-3]}***@**{split_email[1][2:]}'


print(hide_email(mail))