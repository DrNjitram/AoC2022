from collections import defaultdict


def iteration(f: defaultdict, r):
    new_f = defaultdict(list)
    moved = False

    for (x, y), v in list(f.items()):
        if v != 1:
            continue
        elif all([f[(x + dx, y + dy)] == 0 for dx, dy in neighbours_8]):
            new_f[(x, y)] += [(x, y)]
        else:
            for i in range(len(rules)):
                (mx, my), condition = rules[(r + i) % len(rules)]
                if all([f[(x + dx, y + dy)] == 0 for dx, dy in condition]):
                    new_f[(x + mx, y + my)] += [(x, y)]
                    moved = True
                    break
            else:
                new_f[(x, y)] += [(x, y)]

    final_f = defaultdict(int)
    for p, es in new_f.items():
        if len(es) == 1:
            final_f[p] = 1
        else:
            for e in es:
                final_f[e] = 1

    return final_f, moved


def print_map(f):
    limits = [(min(l), max(l)) for l in list(zip(*f.keys()))]
    print(limits)
    for y in range(limits[1][0] - 1, limits[1][1] + 1):
        print("".join([{0: ".", 1: "#"}[f[(x, y)]] for x in range(limits[0][0] - 1, limits[0][1] + 1)]))
    print()


rules = [
    ((0, -1), ((0, -1), (-1, -1), (1, -1))),  # North
    ((0, 1),  ((0, 1),  (-1, 1),  (1, 1))),  # South
    ((-1, 0), ((-1, 0), (-1, 1),  (-1, -1))),  # West
    ((1, 0), ((1, 0), (1, 1), (1, -1)))  # East
]

neighbours_8 = [
    (1, 0), (-1, 0), (0, 1), (0, -1),  # Orthogonal
    (-1, -1), (1, -1), (1, 1), (-1, 1)  # Cardinal
]

field = defaultdict(int)

lines = [l.strip() for l in open("d23.txt").readlines()]

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            field[(x, y)] = 1

starting_elves = sum(field.values())
move_made = True

i = 0
while move_made:
    field, move_made = iteration(field, i)
    i += 1
    if i == 10:
        maxs = [(min(l), max(l)) for l in list(zip(*field.keys()))]
        print(f"P1: {(maxs[0][1] - maxs[0][0]) * (maxs[1][1]-maxs[1][0]) - starting_elves}")

print(f"P2: {i}")

