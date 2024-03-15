from math import sqrt, pi, exp
import matplotlib.pyplot as plt


result = []
with open('result.txt', 'r') as result_file:
    for row in range(10000):
        result.append(float(result_file.readline()))

g = [result.count(e) for e in set(result)]
p = [g[i] / len(result) for i in range(len(g))]

M = 0
for i in range(len(g)):
    M += g[i] * p[i]


Mg2 = 0

for i in range(len(g)):
    Mg2 += (g[i] ** 2) * p[i]

D = Mg2 - M ** 2
x = sqrt(D)

print(f'Матожидание: {M}')
print(f'Дисперсия: {D}')
print(f'Средне-квадратичное отклонение: {x}')
print(f'Минимальное значение: {min(result)}')
print(f'Максимальное значение: {max(result)}')
print(f'Уникальных значений в выборке: {len(set(result))}/{len(result)}')
print(f'Наиболее встречаемое число: {result[g.index(max(g))]}, {max(g)} раз')

left = sorted(p[:len(p) // 2])
right = sorted(p[len(p) // 2:])
right.reverse()

fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(g, range=(0, 5), weights=p, bins=range(0, 10, 1))
ax.set_title('Распределение')
plt.show()

