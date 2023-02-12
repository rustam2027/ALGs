def divide(x, y):
    answer = 0

    if y == 0:
        raise ZeroDivisionError

    while x and x >= y:
        temp_x = x
        counter = 0

        while (temp_x >> 1) > y:
            counter += 1
            temp_x = temp_x >> 1

        x = x - y * (2 ** counter)
        answer += 2 ** counter

    return answer
    
for i in range(1, 5000):
    for j in range(1, 5000):
        assert i // j == divide(i, j), f"Error: {i // j} != {divide(i, j)}"