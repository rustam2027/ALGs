from random import randint

for number in range(2, 11):
    with open(f"test_{number - 1}", "w") as file:
        for i in range(2 ** number):
            for j in range(2 ** number):
                file.write(str(randint(1, 100)) + ' ')
            file.write("\n")