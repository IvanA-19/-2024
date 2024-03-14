from datetime import datetime
import numpy as np
from random import choice


def get_seed():
    seed = bin(int(str(datetime.now()).replace('-', '').
                   replace(' ', '').replace(':', '').
                   replace('.', '')) // int(str(datetime.now().microsecond)))
    return seed


class Random:
    def __init__(self, a, m, c, seed):
        self.a = a
        self.m = m
        self.c = c
        self.seed = seed

    def get_decomposition(self):
        seed = list(self.seed)
        decomposition = seed
        for _ in range(1000):
            decomposition = (seed[((len(seed) - 1) // 4):((len(seed) - 1) // 2)] +
                             seed[:((len(seed) - 1) // 4)] +
                             seed[((len(seed) - 1) // 2):((3 * len(seed) - 1) // 4)] +
                             seed[((3 * len(seed) - 1) // 4):])

        decomposition.remove('b')

        d = 10 ** (len(decomposition) - 4)
        x = int(choice([c for c in range(len(decomposition))]))

        decomposition = int(''.join(e for e in decomposition), 8) / d

        a = ((x - decomposition) / np.sqrt(x)) ** 2 if x != 0 else 0

        rnd = (1 / (np.sqrt(2 * np.pi)) * np.exp(-a)) if a != 0 else 0

        rnd *= (d / 10 ** 26)

        return rnd

    def get_rnd(self):
        decomposition = self.get_decomposition()
        rand = (self.a + decomposition - self.c) % self.m
        return rand * 10 ** 7


test_sample = []

for _ in range(10000):
    test_sample.append(Random(4500, 2, 1000, get_seed()).get_rnd())


print(len(test_sample), len(set(test_sample)))
print(test_sample)
