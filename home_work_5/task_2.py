#text = input()


def word_sum(line: list) -> int:
    return len(line.split())


def symbol_sum(line: list) -> int:
    return len(line)


def main(text: str):
    print(word_sum(text))
    print(symbol_sum(text))


