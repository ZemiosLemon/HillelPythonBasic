list_user = list(range(10))
n = int(input())

def shift_elements(line: list, nn: int):
    n = -n % len(line)
    return list_user[n:] + list_user[:n]


shift_elements(list_user, n)


