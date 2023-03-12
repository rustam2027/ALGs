import time
from random import randint


class Matrix:
    def _check_correct_key_(self, key: tuple) -> None:
        if type(key) is not tuple:
            raise TypeError
        
        if key[0] >= self.length1:
            raise KeyError
        
        if key[1] >= self.length2:
            raise KeyError


    def __init__(self, base: list):
        self.index1 = 0
        self.index2 = 0

        self.length1 = len(base)
        self.length2 = len(base[0])

        self.value = base


    def get_submatrix(self, point: tuple, len1: int, len2: int):
        return_matrix = Matrix(self.value)

        return_matrix.index1 = point[1]
        return_matrix.index2 = point[0]

        return_matrix.length1 = len1
        return_matrix.length2 = len2
        
        return return_matrix


    def __getitem__(self, key: tuple) -> int:
        self._check_correct_key_(key)
        
        return self.value[self.index1 + key[0]][self.index2 + key[1]]
    
    
    def __setitem__(self, key: tuple, value: int) -> None:
        self._check_correct_key_(key)
        
        self.value[self.index1 + key[0]][self.index2 + key[1]] = value
        
        
    def __add__(self, other):
        return_matrix = Matrix([[0] * self.length1 for _ in range(self.length2)])

        for i in range(self.length1):
            for j in range(self.length2):
                return_matrix[(i, j)] = self[(i, j)] + other[(i, j)]
        
        return return_matrix
    
    
    def __sub__(self, other):
        return_matrix = Matrix([[0] * self.length1 for _ in range(self.length2)])
        
        for i in range(self.length1):
            for j in range(self.length2):
                return_matrix[(i, j)] = self[(i, j)] - other[(i, j)]
        
        return return_matrix


    def __str__(self) -> str:
        return_string = ""

        for i in range(self.length1):
            for j in range(self.length2):
                return_string += f"{str(self[(i, j)])} "
            return_string += "\n"

        return return_string


def simple_mult(A: Matrix, B: Matrix) -> Matrix:
    C = Matrix([[0] * B.length2 for _ in range(A.length1)])

    for i in range(A.length1):
        for j in range(B.length2):
            for k in range(A.length2):
                C[(i, j)] += A[(i, k)] * B[(k, j)]

    return C


def bad_mult(X: Matrix, Y: Matrix) -> Matrix:
    if X.length1 <= 2 or X.index2 <= 2:
        return simple_mult(X, Y)

    half_N = X.length1 // 2
    remind = X.length1 - half_N

    A = X.get_submatrix((0, 0), half_N, half_N)
    B = X.get_submatrix((half_N, 0), remind, half_N)
    C = X.get_submatrix((0, half_N), half_N, remind)
    D = X.get_submatrix((half_N, half_N), remind, remind)

    E = Y.get_submatrix((0, 0), half_N, half_N)
    F = Y.get_submatrix((half_N, 0), remind, half_N)
    G = Y.get_submatrix((0, half_N), half_N, remind)
    H = Y.get_submatrix((half_N, half_N), remind, remind)

    A1 = bad_mult(A, E) + bad_mult(B, G)
    B1 = bad_mult(A, F) + bad_mult(B, H)
    C1 = bad_mult(C, E) + bad_mult(D, G)
    D1 = bad_mult(C, F) + bad_mult(D, H)

    for i in range(half_N):
        A1.value[i] += B1.value[i]

    for i in range(X.length1 - half_N):
        C1.value[i] += D1.value[i]

    A1.value += C1.value
    
    A1.index1 = 0
    A1.index2 = 0
    A1.length1 += B1.length1
    A1.length2 += C1.length2

    return A1


def sum_mult(X: Matrix, Y: Matrix, buffer: Matrix, sign = 1) -> Matrix:
    assert X.length1 == Y.length1 and X.length2 == Y.length2, "Wrong Matrix size"

    buffer.length1 = X.length1
    buffer.length2 = X.length2

    for i in range(X.length1):
        for j in range(X.length2):
            if sign:
                buffer[(i, j)] = X[(i, j)] + Y[(i, j)]
            else:
                buffer[(i, j)] = X[(i, j)] - Y[(i, j)]

    return buffer


def strassen_mult(X: Matrix, Y: Matrix) -> Matrix:
    N = X.length1
    buffer = [Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)])]
    
    return strassen_mult_recursion(X, Y, buffer)


def strassen_mult_recursion(X: Matrix, Y: Matrix, buffer: list) -> Matrix:
    if X.length1 <= 2 or X.index2 <= 2:
        return simple_mult(X, Y)

    half_N = X.length1 // 2
    remind = X.length1 - half_N

    A = X.get_submatrix((0, 0), half_N, half_N)
    B = X.get_submatrix((half_N, 0), remind, half_N)
    C = X.get_submatrix((0, half_N), half_N, remind)
    D = X.get_submatrix((half_N, half_N), remind, remind)

    E = Y.get_submatrix((0, 0), half_N, half_N)
    F = Y.get_submatrix((half_N, 0), remind, half_N)
    G = Y.get_submatrix((0, half_N), half_N, remind)
    H = Y.get_submatrix((half_N, half_N), remind, remind)

    P1 = strassen_mult_recursion(A, F - H, buffer)
    P2 = strassen_mult_recursion(A + B, H, buffer)
    P3 = strassen_mult_recursion(C + D, E, buffer)
    P4 = strassen_mult_recursion(D, G - E, buffer)
    P5 = strassen_mult_recursion(A + D, E + H, buffer)
    P6 = strassen_mult_recursion(B - D, G + H, buffer)
    P7 = strassen_mult_recursion(A - C, E + F, buffer)

    Q1 = sum_mult(sum_mult(sum_mult(P5, P4, buffer[0]), P2, buffer[0], 0), P6, buffer[0])
    Q2 = sum_mult(P1, P2, buffer[1])
    Q3 = sum_mult(P3, P4, buffer[2])
    Q4 = sum_mult(sum_mult(sum_mult(P1, P5, buffer[3]), P3, buffer[3], 1), P7, buffer[3], 1)
    
    ret = Matrix([[0] * Y.length2 for _ in range(X.length1)])
    
    ret.value = Q1.value

    for i in range(half_N):
        ret.value[i] += Q2.value[i]

    for i in range(X.length1 - half_N):
        ret.value[i] += Q4.value[i]

    ret.value += Q3.value

    return ret


ALGS = [simple_mult, bad_mult, strassen_mult]


if __name__ == "__main__":
    N = 2 ** 7
    X = Matrix([[randint(1, 100)] * N for _ in range(N)])
    
    buffer = [Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)]), Matrix([[0] * N for _ in range(N)])]
    
    start1 = time.time()
    Y = bad_mult(X, X)
    end2 = time.time()
    Z = simple_mult(X, X)
    end3 = time.time()
    W = strassen_mult(X, X)
    end4 = time.time()
    print(Z)
    print(Y)
    print(W)
    print(end2 - start1, end3 - end2, end4 - end3)