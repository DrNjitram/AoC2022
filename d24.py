from collections import defaultdict
from queue import LifoQueue
import numpy as np


def complex_mod(a, b):
    return complex(np.real(a) % np.real(b), np.imag(a) % np.imag(b))


def print_map(f, b, d=0):
    for i in range(limits[1]):
        s = ""
        for j in range(limits[0]):
            if f[coord := complex(j, i)] == 1:
                s += "#"
            elif coord in b:
                bs = b[coord]
                if len(bs) == 1:
                    s += rev_d_map[bs[0]]
                else:
                    s += str(len(bs))
            elif position == (coord, d):
                s += 'E'
            else:
                s += "."
        print(s)
    print()


def recursive(curr, t):
    global best
    if D[curr] or curr[2] > best:
        return

    D[curr] = True

    if curr[:2] == t:
        best = min(curr[2], best)
        return

    for neighbor in [(curr[0] + dx, curr[1] + dy, curr[2] + 1) for (dx, dy) in
                     [(1, 0), (-1, 0), (0, -1), (0, 1), (0, 0)]]:
        if not D[neighbor] and field[neighbor[:2]] != 1 and neighbor[1] >= 0 and neighbor not in z_blizzards:
            recursive(neighbor, t)


dir_map = {">": 1, "<": -1, "^": -1j, "v": 1j}
rev_d_map = {v: k for k, v in dir_map.items()}

field = defaultdict(int)  # walls
blizzards = defaultdict(list)  # position: blizzards there (dir)

lines = [l.strip() for l in open("d24.txt").readlines()]
limits = [len(lines[0]), len(lines)]
position = (0, 0)  # complex x, y and depth
target = (0, 0)

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            field[complex(x, y)] = 1
        elif lines[y][x] != '.':
            blizzards[complex(x, y)] += [dir_map[lines[y][x]]]
        elif position == (0, 0):
            position = (x, y, 0)
        elif target == (0, 0) and y == len(lines) - 1:
            target = (x, y)

print_map(field, blizzards)
z_blizzards = defaultdict(list, {(k, 0): v for k, v in blizzards.items()})
depth = 1
while True:
    new_blizzards = defaultdict(list)
    for p, bs in blizzards.items():
        for b in bs:
            new_p = p + b
            if field[new_p] == 1:
                new_p = complex_mod((p + 3 * b), complex(limits[0], limits[1]))

            new_blizzards[new_p] += [b]
            z_blizzards[(new_p, depth)] += [b]
    blizzards = new_blizzards

    print(f"Minute {depth}")

    if depth == 900:
        break

    depth += 1

z_blizzards = {(int(np.real(p)), int(np.imag(p)), d) for (p, d), b in z_blizzards.items()}
field = defaultdict(int, {(int(np.real(p)), int(np.imag(p))): v for p, v in field.items()})
total = []

D = defaultdict(bool)
best = depth

recursive(position, target)
print(best)
total.append(best)

D.clear()
best = depth

recursive((target[0], target[1], total[-1]), position[:2])
print(best)
total.append(best)

D.clear()
best = depth

recursive((position[0], position[1], total[-1]), target)
print(best)

#  585 too low
#  880 too high
