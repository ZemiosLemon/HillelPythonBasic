def dict_none(ggg: dict) -> dict:
    ggg_dict = {k: v for k, v in ggg.items() if v is not None}
    return ggg_dict


print(dict_none({'first_color': 'Red', 'second_color': 'Green', 'third_color': None}))