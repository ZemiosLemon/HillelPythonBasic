import random

counter = 3
while counter:
    chance = int(input('Введите число от 1 до 10:\n'))
    if chance not in range(1, 11):
        print('Error:Вы ввели  число за пределами диапозона!!!')
    else:
        if chance == random.randint(1, 11):
            print('You won!')
            break
        else:
            print('You lose!')
            counter -= 1
