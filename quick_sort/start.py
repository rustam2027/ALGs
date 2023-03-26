import subprocess as sp
from random import randint
import os

MIN_SIZE = 15
MAX_SIZE = 16
NUMBER_OF_ITERATIONS = 5

files = ["/branchfree_lomuto",
         "/standart_hoare",
         "/standart_lomuto"]

test_path = "/Users/rustamsalimov/Documents/GitHub/ALGs/quick_sort/test"

output_path = "/Users/rustamsalimov/Documents/GitHub/ALGs/quick_sort/out.txt"

array = {}

os.chdir("/Users/rustamsalimov/Documents/GitHub/ALGs/quick_sort")


def get_average(data: list) -> float:
    return sum(data) / len(data)


def get_root_mean(data: list) -> float:
    average = get_average(data)

    result: float = 0
    for num in data:
        result += (num - average) ** 2

    result = result / len(data)
    result = result ** 0.5

    return result


def get_geometric_mean(data: list):
    result: float = 1
    for num in data:
        result *= num

    result = result ** (1/len(data))

    return result


for size in range(MIN_SIZE, MAX_SIZE):
    for _ in range(NUMBER_OF_ITERATIONS):
        with open(test_path, "w") as input:
            for i in range(2 ** size):
                input.write(f"{randint(1, 100)} ")
            input.write("\n")

        for file in files:
            sp.run([f".{file}", test_path])
            with open(output_path, "r") as output:
                time = float(output.readline().strip())

            if file not in array:
                array[file] = {}

            if size not in array[file]:
                array[file][size] = [time]
            else:
                array[file][size].append(time)

for file in array:
    for size in array[file]:
        array[file][size] = get_geometric_mean(array[file][size])

print(array)
