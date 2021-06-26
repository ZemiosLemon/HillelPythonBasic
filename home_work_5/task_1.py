def is_prime(a: int) -> bool:
    bool_prime = True
    sum_prime = 0
    for num in range(1, a + 1):
        if a % num == 0:
            sum_prime += 1
            if sum_prime > 2:
                bool_prime = False
            else:
                bool_prime = True
    return bool_prime




