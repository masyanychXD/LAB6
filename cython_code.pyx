import math
import timeit
#from  Cython import *


cpdef bint is_perfect_square(n):
    """Проверяет, является ли число полным квадратом."""
    cdef long long root = int(math.isqrt(n))
    return root * root == n


cpdef tuple fermat_factorization(N):
    cdef long long x, y_squared, y
    """Разложение числа N на множители методом Ферма."""
    if N % 2 == 0:
        return 2, N // 2  # Если N четное, делим на 2

    x = math.isqrt(N) + 1  # Начинаем с ближайшего целого числа к √N
    while True:
        y_squared = x * x - N
        if is_perfect_square(y_squared):
            y = int(math.isqrt(y_squared))
            return (x - y, x + y)  # Возвращаем найденные множители
        x += 1  # Увеличиваем x


# Пример использования
if __name__ == '__main__':
    # TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959, 99999971, 3000009, 700000133,
    #             61335395416403926747]
    #
    # res = [fermat_factorization(i) for i in TEST_LST]
    # print(res)
    time_res = timeit.repeat("res = [fermat_factorization(i) for i in TEST_LST];",
                  setup='import math; from cython_code import is_perfect_square; from cython_code import fermat_factorization; TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959, 99999971, 3000009, 700000133]',
                  number=1, repeat=1)
    print(time_res)
# print(f"Множители числа {N}: {factors}")