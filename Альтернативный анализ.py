from math import sqrt, pi, exp, factorial
import matplotlib.pyplot as plt


result = []
with open('test1.txt', 'r') as result_file:
    for row in range(10000):
        result.append(float(result_file.readline()))

g = [result.count(e) for e in set(result)]
p = [(1 / 10000) * (1 / g[i]) for i in range(len(g))]

p = list(set(p))
g = list(set(g))
p0 = list(p)
g0 = list(g)
g0.sort()
p0.sort()


M = 0
for i in range(len(g)):
    M += g[i] * p[i]


Mg2 = 0

for i in range(len(g)):
    Mg2 += (g[i] ** 2) * p[i]

f = [(((factorial(len(g0))) / (factorial(g0[i]) * factorial(len(g0) - g0[i]))) * p0[i] ** g0[i] * (1 - p0[i]) ** (len(g0) - g0[i])) for i in range(len(g0))]
print(f)
D = Mg2 - M ** 2
x = sqrt(D)

print(f'Матожидание: {M}')
print(f'Дисперсия: {D}')
print(f'Средне-квадратичное отклонение: {x}')
print(f'Минимальное значение: {min(result)}')
print(f'Максимальное значение: {max(result)}')
print(f'Уникальных значений в выборке: {len(set(result))}/{len(result)}')
print(f'Наиболее встречаемое число: {result[g.index(max(g))]}, {max(g)} раз')

fig, ax = plt.subplots(2, figsize=(12, 7))

ax[0].hist(g0, weights=f, bins=range(0, len(g0), 1))
ax[0].set_title(f'Плотность')

ax[1].hist(g0, weights=p0, bins=range(0, len(g), 1))
ax[1].set_title(f'Распределение')


plt.show()

