def third_character(line: list) -> str:
    return line[2]


def penultimate(line: list) -> str:
    return line[-2]


def firs_five(line: list) -> list:
    return line[0:5]


def without_the_last_two(line: list) -> list:
    return line[0:-2]


def even_numbers(line: list) -> list:
    return line[2:-1:2]


def odd_numbers(line: list) -> list:
    return line[1:-1:2]


def reverse_list(line: list) -> list:
    return line[::-1]


def reverse_in_one(line: list) -> list:
    return line[::-2]


def lengths_list(line: list) -> int:
    return len(line)


def main(some_line: list):
    call_functions = [third_character(some_line), penultimate(some_line), firs_five(some_line),
                      without_the_last_two(some_line), even_numbers(some_line), odd_numbers(some_line),
                      reverse_list(some_line), reverse_in_one(some_line), lengths_list(some_line)]
    for num in call_functions:
        print(num)


main(list(range(0, 21)))
