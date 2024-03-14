from math import trunc, sqrt
from random import randint


def func(n):
    if n <= 0:
        return 'Нет чисел'

    arr = [i for i in range(n + 1)]

    for i in range(2, n // 2):
        if arr[i] != 0:
            for j in range(2 * i, n + 1, i):
                arr[j] = 0

    arr = set(arr)
    arr.remove(0)
    return arr


test = [randint(0, 100) for _ in range(100)]

for sample in test:
    print(f'n = {sample}, result: {func(sample)}')

