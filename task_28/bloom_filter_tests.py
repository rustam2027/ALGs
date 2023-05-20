from bloom_filter import BloomFilter
from random import randint


TESTS: list[tuple] = [(['232.60.118.95', '229.166.134.182', '248.44.70.10', '40.193.146.207', '95.244.62.188', '106.47.155.15', '100.21.59.195', '69.252.65.64', '174.64.64.117', '24.3.184.97'], 0.02),
                      (['204.54.224.188', '89.242.51.186', '66.98.118.25', '107.22.147.179', '246.30.122.78', '248.216.127.91', '199.58.129.27', '227.83.108.54', '133.215.110.159', '175.131.128.155', '156.239.26.91', '156.2.152.175', '200.27.97.202', '72.198.61.164', '66.174.116.53', '147.179.41.96', '122.189.173.106', '19.240.75.156', '29.19.249.179', '56.128.18.178'], 0.02),
                      (['178.95.167.184', '1.0.43.144', '19.3.178.78', '133.28.53.152', '77.232.131.162', '185.117.23.71', '57.67.32.108', '156.209.168.13', '154.190.74.70', '240.89.222.68', '8.204.109.72', '9.84.175.161', '140.8.208.144', '111.170.212.69', '68.151.160.127', '71.61.58.4', '13.221.80.73', '30.139.153.128', '206.145.58.199', '16.238.129.192', '111.37.33.23', '185.141.76.249', '160.209.55.81', '148.249.156.128', '249.123.149.246', '83.115.57.6', '111.243.225.204', '234.5.72.80', '143.7.63.51', '159.96.54.147'], 0.002)]


def generate():
    return f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"


def get(num: int) -> None:
    arr, freq = TESTS[num]

    test_filter = BloomFilter(len(arr), freq)
    for address in arr:
        test_filter.add(address)

    for address in arr:
        assert test_filter.look_up(address)

    errors = 0
    counter = 0

    while counter <= 1000:
        address = generate()
        if address not in arr:
            if test_filter.look_up(address):
                errors += 1
            counter += 1

    if ((errors / counter) - freq) > freq / 10:
        print(f"Not enough accuracy: needed {freq}, actual {errors / counter}")
        assert False


def generate_addresses(num):
    ret = []

    while len(ret) < num:
        address = generate()
        if address not in ret:
            ret.append(address)

    return ret


def test0():
    get(0)


def test1():
    get(1)


def test2():
    get(2)


print(generate_addresses(30))
