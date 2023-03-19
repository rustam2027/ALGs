from random import randint
from LSD import sort_strings

TEST_ARRAY = ['XxVNJH_BWn^\\cwcf',
              'HK[KfdqiuJ\\CmYFL',
              'vITtD`gJmzhdWeGh',
              'HwFa`YJ_dUNsoicJ',
              'K_y_dmeLFhXCOtpt',
              'zyu\\HvotAYvDOCpt',
              'gGIe`SEA]gbuMM^]',
              'pBXrlNHmIPZyMHeH',
              'AW^`_xeSTZnEbcnT',
              'gATNUVZsypMbONCK']


def start():
    global TEST_ARRAY

    len_words = randint(1, 50)
    count = 10
    TEST_ARRAY = []

    for _ in range(count):
        TEST_ARRAY.append(chr(randint(65, 122)))
        for _ in range(len_words):
            TEST_ARRAY[-1] += chr(randint(65, 122))


def test_1():
    assert sort_strings(TEST_ARRAY[0]) == sorted(TEST_ARRAY[0])


def test_2():
    assert sort_strings(TEST_ARRAY[1]) == sorted(TEST_ARRAY[1])


def test_3():
    assert sort_strings(TEST_ARRAY[2]) == sorted(TEST_ARRAY[2])


def test_4():
    assert sort_strings(TEST_ARRAY[3]) == sorted(TEST_ARRAY[3])


def test_5():
    assert sort_strings(TEST_ARRAY[4]) == sorted(TEST_ARRAY[4])


def test_6():
    assert sort_strings(TEST_ARRAY[5]) == sorted(TEST_ARRAY[5])


def test_7():
    assert sort_strings(TEST_ARRAY[6]) == sorted(TEST_ARRAY[6])


def test_8():
    assert sort_strings(TEST_ARRAY[7]) == sorted(TEST_ARRAY[7])


def test_9():
    assert sort_strings(TEST_ARRAY[8]) == sorted(TEST_ARRAY[8])


def test_10():
    assert sort_strings(TEST_ARRAY[9]) == sorted(TEST_ARRAY[9])
