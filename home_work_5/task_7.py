import datetime
d = int(input())
m = int(input())
y = int(input())





def is_date(date: int, month: int, year: int):
try:
    date_obj = datetime.date(y, m, d)
    return True
except ValueError:
    return False


#date_obj-date.today()
