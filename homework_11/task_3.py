list_user = list(range(1, 11))
n = int(input())


def shift_elements(line: list, num: int):
    return line[num:] + line[:num]


print(shift_elements(list_user, n))


