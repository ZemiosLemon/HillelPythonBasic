list_ten = list(range(10, 51, 10))
list_revers = []
for digit in range(10, 51, 10):
    list_revers.append(list_ten.pop(-1))
print(list_revers)