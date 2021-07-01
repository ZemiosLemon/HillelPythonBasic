def area(size_1: int, size_2: int, share='3') -> int:
    if share == '3':
        s = 0.5 * size_1 * size_2
        return s
    else:
        s = size_1 * size_2
        return s
