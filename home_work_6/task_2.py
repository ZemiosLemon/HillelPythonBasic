import time


def countdown(func):
    def return_time():
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
