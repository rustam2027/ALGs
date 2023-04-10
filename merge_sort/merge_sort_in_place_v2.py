from math import floor


def sort_array(array: list) -> None:
    N = int((len(array) - 1) / 2) - 1
    sorted_part_index = len(array) - N - 1
    
    assert N != sorted_part_index

    std_merge_sort(array, 0, N, sorted_part_index, False)

    sort_recursion(array, sorted_part_index)


def sort_recursion(array: list, sorted_index: int):
    if sorted_index < 2:
        while (sorted_index):
            i = sorted_index
            while i < len(array) and array[i - 1] > array[i]:
                swap(array, i, i - 1)
                i += 1
            sorted_index -= 1
        return 0
    
    pivot = int(sorted_index / 2) - 1

    std_merge_sort(array, 0, pivot, pivot + 1, 1)

    merge(array, 0, pivot, sorted_index, len(array) - 1, sorted_index - pivot - 1, False)
    sort_recursion(array, sorted_index - pivot - 1)


def swap(array: list, i: int, j: int) -> None:
    array[i], array[j] = array[j], array[i]


def merge(array: list,
          left_1: int,
          right_1: int,
          left_2: int,
          right_2: int,
          buffer: int,
          need_to_return: bool) -> None:
    i = left_1
    j = left_2
    k = buffer

    while i <= right_1 and j <= right_2:
        if array[i] < array[j]:
            swap(array, k, i)
            i += 1
        else:
            swap(array, k, j)
            j += 1
        k += 1

    while i <= right_1:
        swap(array, k, i)
        i += 1
        k += 1

    while j <= right_2:
        swap(array, k, j)
        j += 1
        k += 1

    if need_to_return:
        for iter in range(right_1 - left_1 + right_2 - left_2 + 2):
            swap(array, left_1 + iter, buffer + iter)


def std_merge_sort(array: list, left: int, right: int, buffer: int, need_to_return: bool) -> None:
    if right - left <= 0:
        if not need_to_return:
            swap(array, left, buffer)
        return 0
    elif right - left == 1:
        if array[left] > array[right]:
            swap(array, left, right)
        if not need_to_return:
            swap(array, left, buffer)
            swap(array, right, buffer + 1)
        return 0

    std_merge_sort(array, left, (left + right) // 2, buffer, need_to_return + 1)
    std_merge_sort(array, ((left + right) // 2) + 1, right, buffer, need_to_return + 1)

    merge(array, left, (left + right) // 2, ((left + right) // 2) + 1, right, buffer, need_to_return)


a = [5, 2, 6]
# a = [9, 8, 7, 6, 4, 13, 6]
sort_array(a)
print(a)
