def recursion_divide(x, y, z):
    y = int(y)

    while int(z) < y and len(x) > 0:
        if len(x) == 0:
            return 0
        z = z + x[0]
        x = x[1:]
    
    z = int(z)

    for i in range(0, 12):
        if z < (i + 1) * y:
            break

    if i == 10:
        raise ValueError

    if len(x) > 0:  
        return i * 10 + recursion_divide(str(x), str(y), str(z - y*i))
    else:
        return i


def divide(x, y):
    if x < y:
        return 0
    else:
        return recursion_divide(str(x), str(y), '0')


print(divide(90000000000000, 9))