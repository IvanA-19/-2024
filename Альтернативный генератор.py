from random import choice
from datetime import datetime, date
from math import factorial


def get_binary_string():
    start_point = date(1999, 1, 1)
    today = map(int, str(datetime.today().date()).split('-'))
    binary_string = bin(int(str(datetime.now()).replace('-', '').
                            replace(' ', '').replace(':', '').
                            replace('.', '')) // int(str(datetime.now().microsecond)))

    return str(binary_string).replace('b', '')


def get_decomposition(binary_string):
    decomposition = binary_string
    for _ in range(128):
        temp_str = (binary_string[(len(binary_string) // 4):(len(binary_string) // 2)] +
                    binary_string[(3 * len(binary_string) // 4):] +
                    binary_string[:len(binary_string) // 4] +
                    binary_string[(len(binary_string) // 2):3 * (len(binary_string) // 4)])
        binary_string = temp_str
        decomposition = binary_string

    n = 30
    k = choice([j for j in range(1, n + 1)])
    p = 0.6
    q = 0.4
    d = ((factorial(n) / (factorial(k) * factorial(n - k))) * (p ** k) * (q ** (n - k)))
    if d == 0:
        d = 1

    rnd = int(decomposition, 2) * d * 10 ** -8

    return rnd


test = [get_decomposition(get_binary_string()) for _ in range(10000)]

with open('test1.txt', 'w') as file:
    for num in test:
        file.write(str(num) + '\n')
