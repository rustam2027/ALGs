from Beep import Beep
from random import randint


def shuffle(nums: list):
    for i in range(len(nums)):
        j = randint(0, len(nums) - 1)
        nums[i], nums[j] = nums[j], nums[i]


ARRAYS = [[1, 2, 3, 4, 5, 6],
          [9, 8, 5, 7, 2, 5, 7, 1],
          [8, 7, 5, 4, 7, 2, 7, 8],
          [6, 7, 4, 3, 1, 3, 4, 6, 8, 2],
          [3, 2, 1],
          [2, 3, 1],
          [1, 2, 3],
          [-10, -9, -8, 3, 4, 4],
          [-10, -4, -4, -6, -4, 4, 4, -6, -4, 0, -10, 2, -9, 4, -10,
           -2, 2, 0, -8, -6, 1, 3, 4, -3, -10, -8, -9, 3]]


def run_test1(test_num: int) -> None:
    heap = Beep(ARRAYS[test_num].copy(), ARRAYS[test_num].copy())

    for num in sorted(ARRAYS[test_num]):
        print(num, heap.peek_min())
        assert num == heap.extract_min()


def run_test2(test_num: int) -> None:
    heap = Beep([], [])

    for num in ARRAYS[test_num]:
        heap.insert(num, num)

    for num in sorted(ARRAYS[test_num]):
        print(num, heap.peek_min())
        assert num == heap.extract_min()


def test_0():
    run_test1(0)


def test_1():
    run_test1(1)


def test_2():
    run_test1(2)


def test_3():
    run_test1(3)


def test_4():
    run_test1(4)


def test_5():
    run_test1(5)


def test_6():
    run_test1(6)


def test_7():
    run_test2(7)


def test_8():
    run_test2(8)


# def test_9():
#     run_test(9)


# def test_10():
#     run_test(10)

if __name__ == "__main__":
    test_4()
