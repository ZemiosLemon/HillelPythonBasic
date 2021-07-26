temp = int(input('Введите температуру:'))
type_temp = input('Введите тип температуры:')


def calc_celsius(temperature: int) -> (int, int, int):
    celsius = temperature
    fahrenheit = temperature * 9 / 5 + 32
    kelvin = temperature + 273.15
    print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')


def calc_fahrenheit(temperature: int) -> (int, int, int):
    fahrenheit = temperature
    celsius = (temperature - 32)/1.8
    kelvin = (temperature - 32) * 5/9 + 273.15
    print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')


def calc_kelvin(temperature: int) -> (int, int, int):
    kelvin = temperature
    fahrenheit = (temperature - 273.15) * 9/5 + 32
    celsius = temperature - 273.15
    print(f'Цельсий: {celsius}\nФаренгейт: {fahrenheit}\nКельвин: {kelvin}')



if type_temp == 'C':
    print(f'Цельсий: {calc_celsius}\nФаренгейт: {calc_celsius}\nКельвин: {calc_celsius}')