def divide(x, y): # Пусть длина x = n, длина y = m (в двоичной системе), худшем случаем будет: x = 11...1; y = 10...0
    answer = 0

    if y == 0:
        raise ZeroDivisionError

    while x and x >= y: # Будет выполнено n + 1 раз
        temp_x = x
        counter = 0

        while (temp_x >> 1) > y: # Будет выполнено n - m раз
            counter += 1
            temp_x = temp_x >> 1

        x = x - y * (2 ** counter) # На вычитания потребуется n операций
        answer += 2 ** counter

    return answer # общее колличество операций: (n + 1) * (n - m + n)
    
for i in range(1, 5000):
    for j in range(1, 5000):
        assert i // j == divide(i, j), f"Error: {i // j} != {divide(i, j)}"