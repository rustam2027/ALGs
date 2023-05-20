from bitarray import bitarray
from math import log
from math import ceil
from math import e
from random import randint


def is_prime(num) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_around(num) -> int:
    while not is_prime(num):
        num += 1
    return num


def hash(ip: str, a: int, b: int, c: int, d: int) -> int:
    arr = [int(i) for i in ip.split('.')]
    return arr[0] * a + arr[1] * b * arr[2] * c + arr[3] * d


def completed_hash(a, b, c, d):
    def new_hash(ip) -> int:
        return hash(ip, a=a, b=b, c=c, d=d)
    return new_hash


def get_funcs(num) -> list:
    ret = []
    for _ in range(num):
        ret.append(completed_hash(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)))
    return ret


class BloomFilter():
    def __init__(self, capacity: int, freq: float):
        capacity = find_prime_around(capacity)
        self.amount_of_hash = ceil(log(freq, 0.5))
        self.bit_per_item = ceil(self.amount_of_hash / log(2, e))

        self.capacity = find_prime_around(self.bit_per_item * capacity)
        self.value = bitarray(self.capacity)
        self.funcs = get_funcs(self.amount_of_hash)

    def add(self, item) -> None:
        for func in self.funcs:
            self.value[func(item) % self.capacity] = 1

    def look_up(self, item) -> bool:
        for func in self.funcs:
            if not self.value[func(item) % self.capacity]:
                return False
        return True


if __name__ == "__main__":
    test = BloomFilter(10, 0.02)
    test.add("192.234.45.45")
    print(test.look_up("192.234.45.44"))
