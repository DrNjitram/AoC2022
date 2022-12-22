from collections import defaultdict


def mov(pos, d):
    x, y = pos
    match d:
        case 1 + 0j:
            x += 1
        case -1 + 0j:
            x -= 1
        case 0 + 1j:
            y -= 1
        case 0 - 1j:
            y += 1
    return x, y


def next(pos, d, skip=True, cube=False):
    x, y = mov(pos, d)
    if cube:
        if jungle[(x, y)] == 0:
            print(x, y)
            print(face[pos], d)
            exit()
        else:
            return x, y
    else:
        pos = (x % maxs[0], y % maxs[1])
        if skip and jungle[pos] == 0:
            while jungle[n := next(pos, d, False, cube)] == 0:
                pos = n
            return n
        else:
            return pos


def move(p, d, cube=False):
    for i, ss in enumerate(steps):
        for j, s in enumerate(ss):
            k = 0
            while k < s and jungle[n := next(p, d, cube=cube)] == 1:
                p = n
                k += 1
            if j != len(ss) - 1:
                d *= 1j
        if i != len(steps) - 1:
            d *= -1j
    return (p[1] + 1) * 1000 + (p[0] + 1) * 4 + (
        3 if d == -1j else 2 if d == -1 else 1 if d == 1j else 0)


jungle = defaultdict(int)
steps = []

lines = open("d22_test.txt").readlines()
position = (0, 0)
direction = 1 + 0j

for y, line in enumerate(lines[:-1]):
    for x, c in enumerate(line[:-1]):
        if position == (0, 0) and c == '.':
            position = (x, y)
        if c in ['.', '#']:
            jungle[(x, y)] = 1 if c == "." else 2

steps = [[int(n) for n in bit.split('L')] for bit in lines[-1].split('R')]

maxs = [max(l) for l in list(zip(*jungle.keys()))]

print(move(position, direction))
face = defaultdict(lambda: " ")

faces = {}
counter = 1
for x, y in jungle.keys():
    if jungle[(x, y)] != 0:
        v = x // 4 + y // 4 * 4
        if v not in faces:
            faces[v] = counter
            counter += 1
        face[(x, y)] = faces[v]

for y in range(maxs[1] + 1):
    print("".join([str(face[(x, y)]) for x in range(maxs[0] + 1)]))

relations = {
    (4, 1): (4, 6, -1j),
    (5, ): (5, 2, 2j),
    (1, ): (1, 2, 2j),
    (3, ): (3, 1, -1j),
    (3, ): (3, 5, 1j),
    (1, ): (1, 6, 2j),
    (2, ): (2, 6, 1j),
    (6, 1j): (4, 6, -1j),
    (5, ): (5, 2, 2j),
    (1, ): (1, 2, 2j),
    (3, ): (3, 1, -1j),
    (3, ): (3, 5, 1j),
    (1, ): (1, 6, 2j),
    (2, ): (2, 6, 1j),
}

print(move(position, direction, True))
