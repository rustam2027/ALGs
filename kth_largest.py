from random import randint


def kth(nums: list, k: int) -> int:
    if len(nums) <= 1:
        return nums[0]

    pivot = randint(0, len(nums) - 1)
    p = partition(nums, pivot)

    if p + 1 == k:
        return nums[p]
    elif p + 1 > k:
        return kth(nums[:p], k)
    else:
        return kth(nums[p + 1:], k - p - 1)


def partition(array: list, pivot: int):
    array[0], array[pivot] = array[pivot], array[0]
    i = 0
    for j in range(1, len(array)):
        if array[j] > array[0]:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[0], array[i] = array[i], array[0]
    return i


print(kth([3, 2, 1, 5, 6, 4], 2))

# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/923567217/
