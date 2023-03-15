def counting_sort(array: list, hash_func, max_element):
    return_array = [0] * len(array)
    count_array = [0] * (hash_func(max_element) + 1)

    for elem in array:
        count_array[hash_func(elem)] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in range(len(array) - 1, -1, -1):
        return_array[count_array[hash_func(array[i])] - 1] = array[i]
        count_array[hash_func(array[i])] -= 1

    return return_array


def sort_strings(array: list):
    iter = 0

    def str_hash_func(line: str):
        return ord(line[len(line) - iter - 1])

    while iter < len(array[0]):
        array = counting_sort(array, str_hash_func, "z" * (iter + 1))
        iter += 1

    return array


A = ["ac", "ab", "zk", "de", "hi", "pl", "cz", "it"]
print(sort_strings(A))
print(sorted(A))
