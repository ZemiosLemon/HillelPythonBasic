def decorate(func):
    def wrapper():
        user_str = func()
        split_line = user_str.split()
        return split_line
    return wrapper


@decorate
def line():
    return input()


print(line())
