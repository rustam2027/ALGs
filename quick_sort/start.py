import subprocess as sp
from random import randint
import os
import sys

MIN_SIZE = 15
MAX_SIZE = 16
NUMBER_OF_ITERATIONS = 6

files = ["branchfree_lomuto",
         "standard_hoare",
         "standard_lomuto"]

TEST_PATH = "test"

OUTPUT_PATH = "out.txt"

try:
    os.chdir("/Users/rustamsalimov/Documents/GitHub/ALGs/quick_sort")

    for file in files:
        sp.run(["gcc", f"{file}.c", "-o", file, "-Ofast"], check=True, capture_output=False)
except (FileNotFoundError, sp.CalledProcessError):
    print("Error of finding file (files)")
    sys.exit()

array = {}


def shuffle(nums: list):
    for i in range(len(nums)):
        j = randint(0, len(nums) - 1)
        nums[i], nums[j] = nums[j], nums[i]


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


try:
    for size in range(MIN_SIZE, MAX_SIZE):
        for _ in range(NUMBER_OF_ITERATIONS):
            with open(TEST_PATH, "w", encoding='utf-8') as inp:
                print(f"Creating test file, size={2 ** size}")
                A = list(range(2 ** size))
                print("Shuffling file")
                shuffle(A)
                print(f"Writing in {TEST_PATH} file")
                for i in range(2 ** size):
                    inp.write(f"{A[i]} ")
                inp.write("\n")

            for file in files:
                print(f"Running tests for {file}")
                sp.run([f"./{file}", TEST_PATH], check=True, capture_output=True)
                with open(OUTPUT_PATH, "r", encoding="utf-8") as output:
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
finally:
    for file in files:
        sp.run(["rm", file], check=False)
    sp.run(["rm", "test"], check=False)
    sp.run(["rm", "out.txt"], check=False)
    print(array)
