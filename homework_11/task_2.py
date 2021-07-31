poli_list = ['ШАЛАШ', 'КАЗАК', 'ДЕД', 'ДОХОД', 'ЛЕД', '13231', 'T E N E T', 'ШАБАШ']


def verification(user_list: list):
    for string in user_list:
        if string == string[::-1]:
            print(string)


verification(poli_list)
# print(verification(poli_list))