import requests
import datetime

city = input('Город:')
days = int(input('Количество дней:'))


def get_list():
    return requests.get('https://api.openweathermap.org/data/2.5/forecast/daily?'
                        f'&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8',
                        params={"cnt": days, "q": city}).json()


def processing_list():
    data = get_list()
    temperature_day = []
    temperature_night = []
    temperature_feels = []
    date_list = []
    for day in data['list']:
        temperature_day.append(str(day['temp']['day']))
        temperature_night.append(str(day['temp']['night']))
        temperature_feels.append(str(day['feels_like']['day']))
        date_list.append(datetime.datetime.fromtimestamp(day['dt']).strftime('%d-%m-%Y'))
    return date_list, temperature_day, temperature_night, temperature_feels


def save_file():
    list_result = processing_list()
    temp_days = list_result[1]
    temp_nights = list_result[2]
    temp_feels_likes = list_result[3]
    date = list_result[0]
    with open(f'{date[0]}-{city}-{days}-days-weather-forecast.txt', 'w') as file:
        file.write(
            'Дата'.ljust(20) + 'Дневная температура'.ljust(20) + 'По ощущениям'.ljust(20) + 'Ночная температура'.ljust(
                20) + '\n')
        for i in range(int(days)):
            file.write(
                date[i].ljust(20) + temp_days[i].ljust(20) + temp_feels_likes[i].ljust(20) + temp_nights[i] + '\n')


save_file()
