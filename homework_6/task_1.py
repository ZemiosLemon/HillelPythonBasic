coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def list_dict(some_list_1: tuple, some_list_2: tuple) -> dict:
    new_dict = dict(zip(some_list_1, some_list_2))
    return new_dict


print(list_dict(coin, code))
