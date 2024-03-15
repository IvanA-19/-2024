from math import sqrt, pi, exp
import matplotlib.pyplot as plt


result = []
with open('result.txt', 'r') as result_file:
    for row in range(10000):
        result.append(float(result_file.readline()))

g = [result.count(e) for e in set(result)]
p = [(1 / 10000) * (1 / g[i]) for i in range(len(g))]

p = list(set(p))
g = list(set(g))
g.sort()
p.sort()

M = 0
for i in range(len(g)):
    M += g[i] * p[i]


Mg2 = 0

for i in range(len(g)):
    Mg2 += (g[i] ** 2) * p[i]

print(M, Mg2)

D = Mg2 - M ** 2
x = sqrt(D)

print(f'Матожидание: {M}')
print(f'Дисперсия: {D}')
print(f'Средне-квадратичное отклонение: {x}')
print(f'Минимальное значение: {min(result)}')
print(f'Максимальное значение: {max(result)}')
print(f'Уникальных значений в выборке: {len(set(result))}/{len(result)}')
print(f'Наиболее встречаемое число: {result[g.index(max(g))]}, {max(g)} раз')

fig, ax = plt.subplots(figsize=(12, 7))

ax.hist(g, weights=p, bins=range(0, len(g), 1))
ax.set_title(f'Распределение')
plt.show()

