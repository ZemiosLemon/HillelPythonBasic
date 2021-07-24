user_text = input()


def main(text: str) -> (int, int):
    words = len(text.split())
    symbols = len(text)
    return words, symbols


print('Количество слов:', main(user_text)[0])
print('Количество символов:', main(user_text)[1])
