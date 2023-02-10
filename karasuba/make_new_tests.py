from random import randint


with open('karasuba/tests.txt', 'w') as file:
    for i in range(20):
        file.write(str(randint(1, 9) * 10**10 + randint(10**9, 10**10)) + ' ' + str(10**11 + randint(10**9, 10**10)))
        file.write('\n')