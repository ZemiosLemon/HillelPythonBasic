poli_list = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', 'ЛЕД', '13231', 'T E N E T', 'ШАБАШ']


def verification(user_list: list) -> bool:
    for string in user_list:
        if string == string[::-1]:
            return True
        else:
            return False


print(verification(poli_list))