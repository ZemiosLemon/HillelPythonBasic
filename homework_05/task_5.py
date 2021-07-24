def square(a: int) -> (int, int, float):
    perimeter = a * 4
    sq = a * a
    d = (2*a)**0.5
    return perimeter, sq, d


print(square(10))
