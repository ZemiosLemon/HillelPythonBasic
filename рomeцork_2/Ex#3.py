speed = int(input('Скорость:'))
time = int(input('Время:'))
if speed > 0:
    finish = speed * time
else:
    finish = 100-(abs(speed * time))
print('Вася остановился на', finish, 'км.')
