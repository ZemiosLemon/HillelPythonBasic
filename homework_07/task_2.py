temp = int(input('Введите температуру:'))
type_temp = input('Введите тип температуры:')


def calc_temp(temperature: int, type_temperature: str) -> None:
    if type_temperature == 'C':
        celsius = temperature
        fahrenheit = temperature * 9 / 5 + 32
        kelvin = temperature + 273.15
        print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')
    elif type_temperature == 'F':
        fahrenheit = temperature
        celsius = (temperature - 32)/1.8
        kelvin = (temperature - 32) * 5/9 + 273.15
        print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')
    elif type_temperature == 'K':
        kelvin = temperature
        fahrenheit = (temperature - 273.15) * 9/5 + 32
        celsius = temperature - 273.15
        print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')
    else:
        print('Error')


calc_temp(temp, type_temp)
