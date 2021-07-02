
import datetime
enter_date = int(input())
enter_month = int(input())
enter_year = int(input())


def is_date(date: int, month: int, year: int):
    try:
        datetime.date(year, month, date)
        return True
    except ValueError:
        return False


print(is_date(enter_date, enter_month, enter_year))
