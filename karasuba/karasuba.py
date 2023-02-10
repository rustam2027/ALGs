def mult(x, y):
    x = str(x)
    y = str(y)
    
    N = max(len(x), len(y))
    
    if N == 1:
        return int(x) * int(y)
    
    if N % 2:
        N += 1
        
    if len(x) < N:
        x = '0' * (N - len(x)) + x
    if len(y) < N:
        y = '0' * (N - len(y)) + y
    
    a = x[0: N // 2]
    b = x[N // 2: ]
    c = y[0: N // 2]
    d = y[N // 2: ]
    
    a1 = mult(a, c)
    a2 = mult(b, d)
    a3 = mult(int(a) + int(b), int(c) + int(d)) - a2 - a1
    
    return (a1 * (10 ** N)) + a2 + (a3 * (10 ** (N // 2)))

    
print(mult(1234, 5678) == 1234 * 5678)    
    