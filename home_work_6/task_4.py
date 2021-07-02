import json


with open('acdc.json') as f:
    file_dict = json.load(f)

    summa = 1
    for num in range(10):
        summa += int(file_dict['album']['tracks']['track'][num]['duration'])
    print(summa)


