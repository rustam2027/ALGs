from karasuba import mult

array = []

array.append(0)

with open('karasuba/tests.txt', 'r') as file:
    for numbers in file.readlines():
        array.append(tuple(map(int, numbers.split())))


def make(n):
    return mult(array[n][0], array[n][1]) == array[n][0] * array[n][1]


def test_0():
    assert mult(1234, 5678) == 1234 * 5678

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
    
def test_10():
    assert make(10)
    
def test_11():
    assert make(11)
    
def test_12():
    assert make(12)
    
def test_13():
    assert make(13)
    
def test_14():
    assert make(14)
    
def test_15():
    assert make(15)
    
def test_16():
    assert make(16)
    
def test_17():
    assert make(17)

def test_18():
    assert make(18)
    
def test_19():
    assert make(19)

def test_20():
    assert make(20)

def test_21():
    assert mult(0, 0) == 0 * 0