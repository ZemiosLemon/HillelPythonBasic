

def celsius(temperature: float, type_temperature: str) -> float:
    if type_temperature == 'C':
        return temperature
    elif type_temperature == 'K':
        return temperature - 273.15
    elif type_temperature == 'F':
        return temperature * 9 / 5 + 32
    else:
        return False


def fahrenheit(temperature: float, type_temperature: str) -> float:
    if type_temperature == 'F':
        return temperature
    elif type_temperature == 'K':
        return (temperature - 273.15) * 9/5 + 32
    elif type_temperature == 'C':
        return temperature * 9 / 5 + 32
    else:
        return False


def kelvin(temperature: float, type_temperature: str) -> float:
    if type_temperature == 'K':
        return temperature
    elif type_temperature == 'C':
        return temperature + 273.15
    elif type_temperature == 'F':
        return (temperature - 273.15) * 9/5 + 32
    else:
        return False


print(celsius(293.15, 'K'))
print(fahrenheit(20, 'C'))
print(kelvin(20, 'C'))
