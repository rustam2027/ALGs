from math import floor, log


def count_len(x):
    counter = 0
    while x:
        x //= 10
        counter += 1
    return counter


def mult(x, y):

    N = max(count_len(x), count_len(y))

    if N <= 2:
        return int(x) * int(y)

    if N % 2:
        N += 1

    a = x // (10 ** (N // 2))
    b = x % (10 ** (N // 2))
    c = y // (10 ** (N // 2))
    d = y % (10 ** (N // 2))

    a1 = mult(a, c)
    a2 = mult(b, d)
    a3 = mult(int(a) + int(b), int(c) + int(d)) - a2 - a1

    return (a1 * (10 ** N)) + a2 + (a3 * (10 ** (N // 2)))

    
print(mult(1234, 5678) == 1234 * 5678)    
    