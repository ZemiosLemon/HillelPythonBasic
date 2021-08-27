import re


def format_number(phone_number: str) -> str:
    match = re.sub(r'.*(\d{3}).*(\d{3}).*(\d{2}).*(\d{2}).*',
                   r'(+38) \1 \2-\3-\4', phone_number)
    if len(match) > 9:
        return match
    else:
        return 'Failed to recognize number'


def main():
    input_number = input()
    print(format_number(input_number))


main()
