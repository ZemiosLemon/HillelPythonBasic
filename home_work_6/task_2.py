import time


def countdown(func):
    def time_return():
        num = 3
        while num:
            print(num)
            time.sleep(1)
            num -= 1
            result = func()
        return result
    return countdown


@countdown
def what_time_is_it_now() -> str:
    return time.strftime('%H:%M')


print(what_time_is_it_now())

#
# def func_count():
#     num = 3
#     while num:
#         print(num)
#         time.sleep(1)
#         num -= 1
#     return
#
#
# print(func_count())
# print(time.strftime('%H:%M'))