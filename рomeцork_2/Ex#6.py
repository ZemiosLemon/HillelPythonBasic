enter_num = float(input())
num = int(abs(enter_num))
new_list = tuple(range(10, 101, 10))
if abs(num) not in new_list:
    print(f'Число {enter_num} в списке отсутствует')
else:
    print(f'Число {num} присутствует в списке')
