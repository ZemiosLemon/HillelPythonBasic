mail = input()


def hide_email(email: str) -> str:
    gggg = email.split('@')
    return f'{gggg[0][0:-3]}***@**{gggg[1][2:]}'


print(hide_email(mail))