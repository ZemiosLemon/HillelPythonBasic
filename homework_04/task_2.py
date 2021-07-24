def user_input() -> list:
    main_list = []
    while True:
        x = int(input('Введите число:'))
        if x == 0:
            break
        main_list.append(x)
    return main_list


def length(main_list: list) -> int:
    counter = 0
    for _ in main_list:
        counter += 1
    return counter


def sum_list(main_list: list) -> int:
    counter = 0
    for num in main_list:
        counter += num
    return counter


def multiplication(main_list: list) -> int:
    counter = 1
    for num in main_list:
        counter *= num
    return counter


def mean(main_list: list) -> float:
    average = sum_list(main_list) / length(main_list)
    return average


def max_list(main_list: list) -> tuple[int, int]:
    maximum = main_list[0]
    for num in main_list:
        if num > maximum:
            maximum = num
    return maximum, main_list.index(maximum)


def even_odd(main_list: list) -> tuple[int, int]:
    even = 0
    odd = 0
    for num in main_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def max_2(main_list: list) -> int:
    maximum_1, maximum_2 = main_list[0], main_list[0]
    for num in main_list:
        if num > maximum_1:
            maximum_2 = maximum_1
            maximum_1 = num
        elif num > maximum_2:
            maximum_2 = num
    return maximum_2


def equally_max(main_list: list) -> int:
    count = 0
    for num in main_list:
        if num == max(main_list):
            count += 1
    return count


def all_func():
    main_list = user_input()
    print(main_list)
    call_all_functions = {'Количество чисел:': length(main_list), 'Сумма чисел:': sum_list(main_list),
                          'Среднее арифметическое чисел:': mean(main_list),
                          'Произведение чисел:': multiplication(main_list),
                          'Количество четных чисел:': even_odd(main_list)[0],
                          'Количество нечетных чисел:': even_odd(main_list)[1],
                          'Максимум:': max_list(main_list)[0], 'Индекс максимума:': max_list(main_list)[1],
                          'Второй максимум:': max_2(main_list),
                          'Количество чисел равных максимуму:': equally_max(main_list)}
    for key, func in call_all_functions.items():
        print(key, func)


all_func()
