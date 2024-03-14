def solution(a, b, c):
    if 'j' in a or 'j' in b or 'j' in c:
        a = complex(a)
        b = complex(b)
        c = complex(c)
    else:
        a = float(a)
        b = float(b)
        c = float(c)
    
    d = b ** 2 - 4 * a * c
    
    if a == 0 and b != 0:
        if c == 0:
            return 0
        return f"x = {- c / b}"
    elif a == 0 and b == 0 and c != 0:
        return "Неверные данные"
    elif a == 0 and b == 0 and c == 0:
        return "х любое"
    else:
        if d == 0:
            return f"x = {-b / (2 * a)}"
        else:
            return f"x1 = {(- b + d ** (1 / 2)) / (2 * a)}, x2= {(- b - d ** (1 / 2)) / (2 * a)}"


test = [[2, 2, 2], [2, 2, -2], [2j, 12, 4j], [0, 0, 1], [0, 1, 0], [1, 0, 0], [2, 2, 0], [0, 3, 4], [-2j, 248, 0]]

for sample in test:
    print(solution(str(sample[0]), str(sample[1]), str(sample[2])))
