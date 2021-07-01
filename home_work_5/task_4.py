# some_list = [randint(10, 20) for i in range(10)]
# def list_for_zero(some_list: list):
from random import randint

some_list = [randint(10, 20) for i in range(10)]

print(some_list)
for i in some_list:
    if i % 2 == 0:
        print(i)
       
    print(i)
print(some_list)


