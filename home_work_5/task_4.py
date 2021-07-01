from random import randint

random_list = [randint(10, 20) for i in range(10)]


def change_num(some_list: list):
    new_list = []
    summa = 0
    for num in some_list:
        if num % 2 == 0:
            new_list.append(num)
        else:
            new_list.append(0)
            summa += 1
    return new_list, summa


print(random_list)
print(change_num(random_list)[0])
print(change_num(random_list)[1])
