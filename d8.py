import itertools

field = [l.strip() for l in open("d8.txt").readlines()]

visible = 0

p1 = sum([sum([any([
            all([field[y][i] < field[y][x] for i in range(x)]),  # x left
            all([field[y][i] < field[y][x] for i in range(x + 1, len(field[0]))]),  # x right
            all([field[i][x] < field[y][x] for i in range(y)]),  # y above
            all([field[i][x] < field[y][x] for i in range(y + 1, len(field))]),  # y below
            any([x == 0, y == 0, x == len(field[0]) - 1, y == len(field) - 1])
        ]) for x in range(len(field[0]))]) for y in range(len(field))])

for x in range(len(field[0])):
    for y in range(len(field)):
        a, b, c, d = 0, 0, 0, 0
        for i in range(x - 1, -1, -1):  # left
            a += 1
            if field[y][i] >= field[y][x]:
                break
        for i in range(x + 1, len(field[0])):  # right
            b += 1
            if field[y][i] >= field[y][x]:
                break
        for i in range(y - 1, -1, -1):  # top
            c += 1
            if field[i][x] >= field[y][x]:
                break
        for i in range(y + 1, len(field)):  # bottom
            d += 1
            if field[i][x] >= field[y][x]:
                break

        visible = max([visible, a * b * c * d])

print(p1, visible)
