words = 'What makes a good man'


def longest_word(line: str) -> str:
    split_line = line.split()
    new_list = []
    max_word = len(split_line[0])
    for num in split_line:
        new_list.append(len(num))
        if len(num) > max_word:
            max_word = len(num)
            return split_line[new_list.index(max_word)]


print(longest_word(words))
