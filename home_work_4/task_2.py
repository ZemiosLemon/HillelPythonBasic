def xxx():
    ls = []
    while True:
        x = int(input())
        if x == 0:
            break
        ls.append(x)
    return ls


def lenn(ls: list) -> int:  # - количество введённых чисел (завершающий 0 не считается)
    counter = 0
    for num in ls:
        counter += 1
    return counter


def summ(ls: list) -> int:  # - их сумму
    counter = 0
    for num in ls:
        counter += num
    return counter


def multiplication(ls: list) -> int:  # - произведение
    counter = 1
    for num in ls:
        counter *= num
    return counter


def mean(ls: list) -> int:  # - среднее арифметическое (не считая завершающего числа 0)
    ave = summ(ls) / lenn(ls)
    return ave


def maxx(
        ls: list) -> tuple[Any, int]:  # '''определить значение и порядковый номер наибольшего элемента последовательности.Если наибольших элементов несколько, выведите порядковый номер первого из них.'''
    maxx = ls[0]
    for num in ls:
        if num > maxx:
            maxx = num
    return maxx, ls.index(maxx)


def even_odd(ls: list) -> int:  # - определить количество чётных и не чётных элементов в последовательности
    even = 0
    odd = 0
    for num in ls:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def max_2(ls: list) -> int:  # - определить значение второго по величине элемента в этой последовательности
    max_1, max_2 = ls[0], ls[0]
    for num in ls:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num
    return max_2


def equally_max(ls: list) -> int:  # - определите, сколько элементов этой последовательности равны ее наибольшему элементу

    count = 0
    for num in ls:
        if num == maxx(ls):
            count += 1
    return count


ls = xxx()
def all_func
print(ls)
print('Количество', lenn(ls))
print('Summ', summ(ls))
print('Среднее', mean(ls))
print('Произведение', multiplication(ls))
print('Чет, нечет', even_odd(ls))
print('Max', maxx(ls))
print('Max 2', max_2(ls))
print('Равно MAX', equally_max(ls))
