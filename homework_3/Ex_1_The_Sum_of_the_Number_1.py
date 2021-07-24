num = int(input('Введите число:'))
sum = 0
while num:
   sum += num %10
   num //= 10
print(f'Сумма цифр числа равна: {sum}')


