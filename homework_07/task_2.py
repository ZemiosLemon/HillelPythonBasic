def user_input() -> (int, str):
    temp = int(input('Введите температуру:'))
    type_temp = input('Введите тип температуры:')
    return temp, type_temp


def calc_temp(temperature: int, type_temperature: str) -> None:
    if type_temperature == 'C':
        f = temperature * 9 / 5 + 32
        k = temperature + 273.15
        print(f'Цельсий: {temperature}\nФаренгейт: {f}\nКельвин: {k}')
    elif type_temperature == 'F':
        c = (temperature - 32)/1.8
        k = (temperature - 32) * 5/9 + 273.15
        print(f'Цельсий: {c}\nФаренгейт: {temperature}\nКельвин: {k}')
    else:
        f = (temperature - 273.15) * 9/5 + 32
        c = temperature - 273.15
        print(f'Цельсий: {c}\nФаренгейт: {f}\nКельвин: {temperature}')


calc_temp(user_input())


temp = int(input('Введите температуру:'))
type_temp = input('Введите тип температуры:')


def calc_temp(temperature: int, type_temperature: str) -> None:
    if type_temperature == 'C':
        f = temperature * 9 / 5 + 32
        k = temperature + 273.15
        print(f'Цельсий: {temperature}\nФаренгейт: {f}\nКельвин: {k}')
    elif type_temperature == 'F':
        c = (temperature - 32)/1.8
        k = (temperature - 32) * 5/9 + 273.15
        print(f'Цельсий: {c}\nФаренгейт: {temperature}\nКельвин: {k}')
    else:
        f = (temperature - 273.15) * 9/5 + 32
        c = temperature - 273.15
        print(f'Цельсий: {c}\nФаренгейт: {f}\nКельвин: {temperature}')


calc_temp(temp, type_temp)