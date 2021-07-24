def fake_string(start_srt: str, replace_word: str, new_word: str,
                number_replace: int) -> str:
    return start_srt.replace(replace_word, new_word, number_replace)


print('DC makes good movies, DC makes good comics')
print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
