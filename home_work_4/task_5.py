str = list(range(1, 21))
print(str)
print(str[2]) #   a. выведите третий символ этой строки.
print(str[-2]) # b. выведите предпоследний символ этой строки.
print(str[0:5]) # c. выведите первые пять символов этой строки.
print(str[0:-2]) # d. выведите всю строку, кроме последних двух символов.
print(str[1:-1:2])#    e. выведите все символы с четными индексами (считая, что индексация начинается с 0,
#    поэтому символы выводятся начиная с первого).
print(str[0:-1:2])#    f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print(str[::-1])#    g. выведите все символы в обратном порядке.
print(str[::-2])#    h. выведите все символы строки через один в обратном порядке, начиная с последнего.
print(len(str))#   i. выведите длину данной строки.