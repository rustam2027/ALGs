from math import ceil
from math import floor


def merge(left_edge_1, right_edge_1, left_edge_2, right_edge_2, return_index, array, need_to_return):
    len_of_arr = right_edge_1 - left_edge_1 + right_edge_2 - left_edge_2 + 2
    return_to = left_edge_1

    iter = 0

    while left_edge_1 <= right_edge_1 and left_edge_2 <= right_edge_2:
        if array[left_edge_1] > array[left_edge_2]:
            array[return_index + iter], array[left_edge_2] = array[left_edge_2], array[return_index + iter]
            left_edge_2 += 1
        else:
            array[return_index + iter], array[left_edge_1] = array[left_edge_1], array[return_index + iter]
            left_edge_1 += 1

        iter += 1

    while left_edge_1 <= right_edge_1:
        array[return_index + iter], array[left_edge_1] = array[left_edge_1], array[return_index + iter]
        left_edge_1 += 1
        iter += 1

    while left_edge_2 <= right_edge_2:
        array[return_index + iter], array[left_edge_2] = array[left_edge_2], array[return_index + iter]
        left_edge_2 += 1
        iter += 1
    
    if need_to_return:
        for i in range(len_of_arr):
            array[return_to + i], array[return_index + i] = array[return_index + i], array[return_to + i]


def recursion(first_index, second_index, return_index, array, need_to_return):
    assert second_index >= first_index, f"{second_index} < {first_index}"

    if second_index - first_index == 0:
        if need_to_return == 0:
            array[return_index], array[first_index] = array[first_index], array[return_index]
        return 0

    if second_index - first_index == 1: 
        if array[first_index] > array[second_index]:
            if need_to_return == 0:
                array[return_index], array[second_index] = array[second_index], array[return_index]
                array[return_index + 1], array[first_index] = array[first_index], array[return_index + 1]
            else:
                array[first_index], array[second_index] = array[second_index], array[first_index]
        else:
            if need_to_return == 0:
                array[return_index], array[first_index] = array[first_index], array[return_index]
                array[return_index + 1], array[second_index] = array[second_index], array[return_index + 1]
        return 0

    pivot = (second_index + first_index) // 2

    recursion(first_index, pivot, return_index, array, need_to_return + 1)
    recursion(pivot + 1, second_index, return_index, array, need_to_return + 1)

    merge(first_index, pivot, pivot + 1, second_index, return_index, array, need_to_return)
    
def recursion_main(sorted_left, sorted_right, not_sorted_left, not_sorted_right, array):
    if not_sorted_right - not_sorted_left + 1 <= 2:
        while not_sorted_left <= not_sorted_right:
            num = array[not_sorted_right]
            flag = True

            for i in range(not_sorted_right + 1, sorted_right + 1):
                if array[i] > num:
                    array[i - 1] = num
                    flag = False
                    break
                else:
                    array[i - 1] = array[i]
            
            if flag:
                array[-1] = num

            not_sorted_right -= 1
        return 0

    pivot = ceil((not_sorted_left + not_sorted_right + 1) / 2)

    len_of_sorted = not_sorted_right - pivot

    recursion(pivot, not_sorted_right, not_sorted_left, array, 0)
    merge(not_sorted_left, not_sorted_left + len_of_sorted, sorted_left, sorted_right, not_sorted_right - len_of_sorted, array, 0)

    recursion_main(sorted_left - len_of_sorted - 1, sorted_right, not_sorted_left, not_sorted_right - len_of_sorted - 1, array)



def sort(array):
    _left_index_ = 0
    _right_index_ = len(array) - 1
    
    if _right_index_ < 1:
        return 0
    pivot = floor((_right_index_) / 2)

    recursion(_left_index_, pivot, _right_index_ - (_left_index_ + pivot), array, 0)
    recursion_main(pivot + 1, _right_index_, 0, pivot, array)

if __name__ == "__main__":
    arr = [-2, 3, -5]
    sort(arr)
    print(arr)