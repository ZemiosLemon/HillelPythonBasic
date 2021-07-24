def dict_none(some_dict: dict) -> dict:
    final_dict = {key: value for key, value in some_dict.items() if value is not None}
    return final_dict


print(dict_none({'first_color': 'Red', 'second_color': 'Green', 'third_color': None}))
