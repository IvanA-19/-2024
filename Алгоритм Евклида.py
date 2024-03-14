from random import randint


def euklid_alg(a, b):
    if a == b == 0:
        return 'Любое число'

    if b == 0:
        a, b = b, a

    q = a // b

    r = a - q * b
    a = b
    b = r

    if r != 0:
        return euklid_alg(a, b)
    else:
        return abs(a)


test = [[randint(-100, 100), randint(-100, 100)] for _ in range(100)]

for sample in test:
    print(f"a, b: {' '.join(str(sample[i]) for i in range(len(sample)))}; НОД: {euklid_alg(*sample)}")

