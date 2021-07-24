user_list = ['a', 'b', 'c', 'd', 'e']


def transforms(line: list) -> dict:
    new_dict = dict(enumerate(line))
    return new_dict


print(transforms(user_list))
