import timeit

import python_code
import cython


numbers = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959, 99999971, 3000009, 700000133, 61335395416403926747, 9576890767]
dif = list(range(1, len(numbers)))
allp=[]
allc=[]


for i in range(12):
    TEST_LST = numbers[:i]

    setupstringp = f'import math; from python_code import is_perfect_square; from python_code import fermat_factorization; {TEST_LST}'
    setupstringc = f'import math; from cython_code import is_perfect_square; from cython_code import fermat_factorization; {TEST_LST}'

    allp.append(timeit.repeat(f"res = [fermat_factorization(i) for i in {TEST_LST}];",
                             setup=setupstringp,
                             number=1, repeat=1))



    allc.append(timeit.repeat(f"res = [fermat_factorization(i) for i in {TEST_LST}];",
                             setup=setupstringc,
                             number=1, repeat=1))

    print(i)




import matplotlib.pyplot as plt


print(len(dif))
print(len(allp))

# Создание scatter plots
plt.figure(figsize=(8, 6))  # Размер графика
plt.plot(dif, allp, 'b-', label='Код на питоне')  # Первый scatter plot
plt.plot(dif, allc, 'r-', label='Код на сайтоне')   # Второй scatter plot

# Настройка графика
plt.title('Сравнение python и cython')
plt.xlabel('Сложность')
plt.ylabel('Время')
plt.legend()  # Добавление легенды
plt.grid(True, linestyle='--', alpha=0.5)  # Сетка

plt.show()