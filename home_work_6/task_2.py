import time
#
#
# def countdown(func):
#     def countdown():
#         num = 3
#         while num:
#             print(num)
#             time.sleep(1)
#             num -= 1
#             result = func()
#         return result
#     return countdown
#
#
# @countdown
# def time_return() -> str:
#     return time.strftime('%H:%M')
#

# print(time_return())


def func_count():
    num = 3
    while num:
        print(num)
        time.sleep(1)
        num -= 1
    return


print(func_count())
print(time.strftime('%H:%M'))