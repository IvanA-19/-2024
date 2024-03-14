def solution(a1, b1, c1, a2, b2, c2):
    d = a1 * b2 - b1 * a2
    d1 = a1 * c2 - c1 * a2
    d2 = b1 * c2 - c1 * b2

    if ((a1 == b1 == 0 and c1 != 0) or (a2 == b2 == 0 and c2 != 0) or
            (a1 == c1 == 0 and b1 != 0) or (b1 == c1 == 0 and a1 != 0) or
            (a2 == c2 == 0 and b2 != 0) or (b2 == c2 == 0 and a2 != 0)):
        return 'Неверные данные'

    if d == 0:
        return 'Бесконечно много решений'

    else:
        return f'x = {d1 / d} y = {d2 / d}'


test = [[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 3, 5],
        [122, 34, 10, -212, 34, 8],
        [2j, 34 + 1j, -12, 0, 4, 5],
        [2, 2, 3, 2, 2, 7],
        [-2, -4, 9, 8, -10, 12]]


for sample in test:
    print(solution(*sample))
