from to_polish import get_polish


def test_1():
    assert get_polish("( 1 + 2 ) * 2 / 3 + 4".split()) == ['1', '2', '+', '2', '*', '3', '/', '4', '+']


def test_2():
    assert get_polish("( ( 2 + 3 ) * 2 + 2 ) * 2".split()) == ['2', '3', '+', '2', '*', '2', '+', '2', '*']


def test_3():
    assert get_polish("( ( ( ( ( ( ( ( 2 + 3 ) ) ) ) ) ) ) )".split()) == ['2', '3', '+']


def test_4():
    assert get_polish("( 1 - 5 ) ^ 3 * 2".split()) == ['1', '5', '-', '3', '^', '2', '*']


def test_5():
    assert get_polish("1".split()) == ['1']


def test_6():
    assert get_polish("( 1 + 2 ) * ( 2 + 3 )".split()) == ['1', '2', '+', '2', '3', '+', '*']


def test_7():
    assert get_polish("( 1 + 2 ) * ( 2 + 3 ) * ( 3 + 4 ) * ( 4 + 5 )".split()) == ['1', '2', '+', '2', '3', '+', '3', '4', '+', '4', '5', '+', '*', '*', '*']
