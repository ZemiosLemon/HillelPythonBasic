list_user = list(range(10))
n = int(input())


def shift_elements(line: list, num: int):
    num = -num % len(line)
    return list_user[n:] + list_user[:n]


print(shift_elements(list_user, n))


