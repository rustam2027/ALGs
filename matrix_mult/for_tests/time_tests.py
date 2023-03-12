from algorithms import *
import time
import math


def display_percent(percent: int) -> None:
    print('\r', f"{percent // 5 * '█'}".ljust(20, "_"), end="")
    print(f" {percent}% ", end="")


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


def format_table(name_column, name_line, data):

    NAME = "Benchmark"
    FOUR = 4 # Two spaces and two separators

    # Find some lens
    lines_len = []
    lines_len.append(max(len(max(name_column, key=lambda x: len(x))),
                         len(NAME)) + FOUR)
    for i in range(len(name_line)):
        
        max_len_value = 0
        
        for j in range(len(name_column)):
            max_len_value = max(len(str(data[j][i])), max_len_value)
        
        lines_len.append(max(len(name_line[i]), max_len_value) + FOUR)

    # Printing
    print(f"|{NAME.center(lines_len[0])}|", end="")
    for i in range(len(name_line)):
        print(f"{name_line[i].center(lines_len[i + 1])}|", end="")

    print()
    print("|", end="")
    for i in range(len(lines_len)):
        print("-" * lines_len[i], "|", sep="", end="")
    print()

    for i in range(len(name_column)):
        print(f"|{name_column[i].center(lines_len[0])}|", end="")
        for j in range(len(name_line)):
            print(f"{str(data[i][j]).center(lines_len[j + 1])}|", end="")
        print()


def get_data(number: int) -> Matrix:
    return_list = []
    with open(f"matrix_mult/for_tests/tests/test_{number}") as file:
        for line in file.readlines():
            return_list.append(list(map(int, line.split())))
    
    return Matrix(return_list)


results: dict = {}

M = 7
N = 8
C = 10

ops = 0
need_ops = C * sum([2 ** i for i in range(M, N)]) * len(ALGS)

display_percent(0)

for test_number in range(M, N):
    data = get_data(test_number)

    for algorithm in ALGS:
        for test in range(C):

            start = time.time_ns()
            algorithm(data, data)
            time_for_test = time.time_ns() - start
            
            if algorithm not in results:
                results[algorithm] = {}

            if test_number not in results[algorithm]:
                results[algorithm][test_number] = []
                
            display_percent(math.ceil((ops / need_ops) * 100))
                
            results[algorithm][test_number].append(time_for_test / 10 ** 6)
            
            ops += 2 ** test_number
            
with open("out.txt", 'a') as file:
    file.write(str(results))
            
print("\r", end="")

names = []
tests_num = [str(2 ** i) for i in range(M, N)]

values = []
            
for alg in results:
    names.append(alg.__name__)
    val_out = []
    for num in results[alg]:
        
        val = str(round(get_average(results[alg][num]), 3)) + ' '+ str(round(get_geometric_mean(results[alg][num]), 3)) + ' ' + str(round(get_root_mean(results[alg][num]), 3))
        
        val_out.append(val)
    values.append(val_out)
        
format_table(names, tests_num, values)
