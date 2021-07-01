from random import randint

some_list = [randint(10, 20) for i in range(10)]


def change_num(some_list: list):
    new_list = []
    sum = 0
    for num in some_list:
        if num % 2 == 0:
            new_list.append(num)
        else:
            new_list.append(0)
            sum += 1
    return new_list, sum


print(change_num(some_list)[0])
print(change_num(some_list)[1])
