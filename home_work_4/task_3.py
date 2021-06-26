def enter_list() -> list:
    a, b = int(input()), int(input())
    if a < b:
        ls = [num for num in range(a, b + 1)]
    else:
        ls = [num for num in range(a, b - 1, -1)]
    return ls


print(enter_list())
