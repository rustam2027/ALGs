import pytest
from  merge_sort_in_place import sort

tests = [[3, 5, 7, 3, 7, 5, 1, 5, 7],
         [1, 1],
         [0, 0, 0, 0],
         [1, 2, 3, 4],
         [6, 7, 8, 9, 1, 5, 1, 8, 3],
         [7, 4, 8, 5, 87, 8, 0],
         [1, 0, 8, 2, 3, 5, 6, 7,2, 5, 6, 7, 1],
         [1],
         [0],
         [9, 4, 6, 9, 3, 1, 7, 5, 7, 2, 3, 5, 9]]

def make(n):
    arr_real = arr_exp = tests[n]
    sort(arr_real)
    arr_exp.sort()
    return arr_real == arr_exp


def test_0():
    assert make(0)

def test_1():
    assert make(1)

def test_2():
    assert make(2)

def test_3():
    assert make(3)
    
def test_4():
    assert make(4)
    
def test_5():
    assert make(5)

def test_6():
    assert make(6)

def test_7():
    assert make(7)
    
def test_8():
    assert make(8)

def test_9():
    assert make(9)
