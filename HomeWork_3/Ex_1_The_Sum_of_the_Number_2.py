num = input('Введите число:')
list_num = list(num)
sum = 0
for digit in range(len(list_num)):
   sum += int(list_num[digit])
print(f'Сумма цифр числа равна: {sum}')
