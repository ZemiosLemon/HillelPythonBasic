def enter_list() -> list:
    a, b = int(input('Enter num A:')), int(input('Enter num B:'))
    if a < b:
        ls = [num for num in range(a, b + 1)]
    else:
        ls = [num for num in range(b, a+1)]
    return ls


print(enter_list())
