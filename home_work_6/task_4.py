import json
import datetime


def duration():
    with open('acdc.json') as f:
        file_dict = json.load(f)
        summa = 0
        for num in range(10):
            summa += int(file_dict['album']['tracks']['track'][num]['duration'])
        return summa


def conversion_in_seconds(func):
    size = datetime.timedelta(seconds=func)
    return size



print(conversion_in_seconds(duration()))

