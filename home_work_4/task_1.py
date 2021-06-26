x = int(input('run first day'))
y = int(input())
sum = 0
while x < y:
    x += (0.1*x)
    sum += 1
    print(x)
    print(sum)