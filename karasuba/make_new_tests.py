from random import randint


with open('karasuba/tests.txt', 'w') as file:
    for i in range(20):
        file.write(str(randint(1, 9) * 10**20 + randint(10**19, 10**20)) + ' ' + str(10**20 + randint(10**19, 10**20)))
        file.write('\n')