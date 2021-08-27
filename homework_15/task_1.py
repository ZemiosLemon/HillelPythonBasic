import csv
import re
#
# x = {'A': 'А', 'B': 'В', 'E': 'Е', 'I': 'І', 'K': 'К', 'M': 'М', 'H': 'Н',
#      'O': 'О', 'P': 'Р', 'C': 'С', 'T': 'Т', 'Y': 'У', 'X': 'Х'}
# toyota = "BH2112СТ".translate(str.maketrans({'A': 'А', 'B': 'В', 'E': 'Е', 'I': 'І', 'K': 'К', 'M': 'М', 'H': 'Н',
#                                             'O': 'О', 'P': 'Р', 'C': 'С', 'T': 'Т', 'Y': 'У', 'X': 'Х'}))


def check_number(auto_number):
    match = re.fullmatch(r'([А-ЯA-Z]){2}\d{4}[А-ЯA-Z]{2}', auto_number)
    if match:
        return auto_number[:2]
    else:
        return 'Не является автомобильным номером'


def get_csv_data():
    with open('ua_auto.csv', mode='r', encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        return list(data)


def auto_region(auto_number, data):
    reg = check_number(auto_number)
    for row in data:
        if row['Код 2004'] == reg or row['Код 2013'] == reg:
            return row['Регіон']
    return 'Регион не найден'


def main():
    user_input = input('Введите номер:').translate(str.maketrans({'A': 'А', 'B': 'В', 'E': 'Е', 'I': 'І', 'K': 'К',
                                                                  'M': 'М', 'H': 'Н', 'O': 'О', 'P': 'Р', 'C': 'С',
                                                                  'T': 'Т', 'Y': 'У', 'X': 'Х'}))
    check_number(user_input)
    print(auto_region(user_input, get_csv_data()))


main()
