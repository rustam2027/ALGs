def recursion_divide(a, b, c):
    result = ''
    counter = 0

    while int(b, 2) > int(c, 2):
        if counter:
            result += '0'

        if not a:
            return result

        if c == '0':
            c = a[0]
        else:
            c += a[0]

        a = a[1:]
        counter += 1
    
    result += '1'
    ost = bin(int(c, 2) - int(b, 2))[2:]

    return result + recursion_divide(a, b, str(ost))

    


def divide(x, y):
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]
    
    return int(recursion_divide(bin_x, bin_y, '0'), 2)


print(divide(234, 5))