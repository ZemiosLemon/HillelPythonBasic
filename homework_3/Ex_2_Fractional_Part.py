num = input('Введите чило:')
list_1 = list(num.split('.'))
list_2 = list(list_1[1])
print('Дробная часть числа:', list_1[1])
print('Первая цифра после точки:', list_2[0])


