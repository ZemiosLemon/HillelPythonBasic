import argparse
import time
import requests
import datetime
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency exchange app')
    parser.add_argument('currency_from')
    parser.add_argument('currency_to')
    parser.add_argument('amount', type=float)
    parser.add_argument('-sd', '--start_date', default=datetime.date.today())
    args = parser.parse_args()


def date_check():
    try:
        datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
        date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
        return date
    except ValueError:
        date = datetime.datetime.now()
        return date


def symbols_check():
    with open('symbols.json', 'r') as file:
        check_list = json.load(file)
        if args.currency_from not in check_list['symbols'] or args.currency_to not in check_list['symbols']:
            return 'USD', 'UAH'
        else:
            return args.currency_from, args.currency_to


def exchange():
    exchange_from, exchange_to = symbols_check()[0], symbols_check()[1]
    final_list = [["date", "from", "to", "amount", "rate", "result"]]
    date_start = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
    while date_start < datetime.datetime.now():
        get_list = requests.get('https://api.exchangerate.host/convert',
                                params={'from': exchange_from, 'to': exchange_to,
                                        'amount': args.amount, 'date': date_start}).json()
        date_start += datetime.timedelta(days=1)
        result_list = [get_list['date'], exchange_from, exchange_to, args.amount, get_list['info']['rate'], get_list['result']]
        final_list.append(result_list)
        time.sleep(1)
    for num in final_list:
        print(num)


exchange()
