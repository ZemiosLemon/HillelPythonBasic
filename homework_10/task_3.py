longest_word_line = 'What makes a good man'


#def longest_word(line: str) -> str:
split_line = line.split()
new_list = []
max_word = len(split_line[0])
for num in split_line:
    new_list.append(len(num))

    if len(num) > max_word:
        max_word = len(num)
        print(filter(filter(max_word, split_line))
        #return split_line[new_list.index(max_word)]


# def cheat_longest_word(line: str) -> str:
#     return max(line.split(), key=len)


# print(longest_word(longest_word_line))
# print(cheat_longest_word(longest_word_line))
