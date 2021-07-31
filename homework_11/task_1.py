def user_input():
    input_list = []
    while True:
        user_enter = input()
        if user_enter == '':
            break
        input_list.append(user_enter)
    return input_list


def write_file():
    user_list = user_input()
    with open(f'create_file.txt.txt', 'w') as file:
        for num in range(len(user_list)):
            file.write(user_list[num] + '\n')


write_file()
