start_position = input('Введите координаты клетки\n'
                       '(a-z,1-8 без пробелов):\n'
                       'Введите начальную позицию фигуры:\n')
final_position = input('Введите конечную позицию фигуры:\n')
start_position_latter = int(ord(list(start_position)[0]))
start_position_digit = int(ord(list(start_position)[1]))
final_position_latter = int(ord(list(final_position)[0]))
final_position_digit = int(ord(list(final_position)[1]))
odds_latter = abs(start_position_latter-final_position_latter)
odds_digit = abs(start_position_digit-final_position_digit)
print(start_position_latter, final_position_latter, start_position_digit, final_position_digit)
if start_position_latter not in range(97, 105) or start_position_digit not in range(49, 57):
    print('Ошибка: Неверный формат ввода.')
elif final_position_latter not in range(97, 105) or final_position_digit not in range(49, 57):
    print('Ошибка: Неверный формат ввода.')
elif odds_latter == 2 and odds_digit == 1 or odds_latter == 1 and odds_digit == 2:
    print('Фигура является конем!')
else:
    print('Фигура НЕ является конем!')
