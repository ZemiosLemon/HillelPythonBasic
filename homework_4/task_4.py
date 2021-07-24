def stairs():
    n = int(input())
    for num in range(1, n+1):
        for val in range(1, num+1):
            print(val, end='')
        print()
    return

stairs()
