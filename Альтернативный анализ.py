from math import sqrt, factorial
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


result = []
with open('test1.txt', 'r') as result_file:
    for row in range(10000):
        result.append(float(result_file.readline()))

g = [result.count(e) for e in set(result)]
p = [(1 / 10) * (1 / g[i]) for i in range(len(g))]

p = list(set(p))
g = list(set(g))

M = 0
for i in range(len(g)):
    M += g[i] * p[i]


Mg2 = 0

for i in range(len(g)):
    Mg2 += (g[i] ** 2) * p[i]

f = [((factorial(10) / (factorial(g[i]) * factorial(10 - g[i]))) * (p[i] ** g[i]) * (1 - p[i]) ** (10 - g[i])) for i in range(len(g))]
D = Mg2 - M ** 2
x = sqrt(D)

print(f'Матожидание: {M}')
print(f'Дисперсия: {D}')
print(f'Средне-квадратичное отклонение: {x}')
print(f'Минимальное значение: {min(result)}')
print(f'Максимальное значение: {max(result)}')
print(f'Уникальных значений в выборке: {len(set(result))}/{len(result)}')
print(f'Наиболее встречаемое число: {result[g.index(max(g))]}, {max(g)} раз')

x0 = np.arange(0, 4, 0.001)
fig, ax = plt.subplots(figsize=(12, 7))

ax.hist(g, weights=f, bins=range(0, 6, 1))
ax.set_title(f'Плотность')
ax.plot(x0, norm.pdf(x0, M, x), color='DarkGreen')

plt.show()

