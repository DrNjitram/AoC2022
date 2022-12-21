import math
from collections import defaultdict


def get_height(c):
    return max([y_val for (_, y_val), val in c.items() if val > 0] + [0]) + 4


def get_col(cave_map, rx, ry):
    if rx % 8 == 0 or ry == 0:
        return 1
    else:
        return cave_map[(rx, ry)]


def no_collision(c, r, xc, yc):
    for ry, rock_row in enumerate(r):
        for rx, val in enumerate(rock_row):
            if val == 1 and get_col(c, xc + rx, yc + ry) > 0:
                return False
    return True


def blow(c, r, rx, ry):
    global step
    new_x = rx + (1 if gasses[step % len(gasses)] == ">" else -1)
    step += 1
    if no_collision(c, r, new_x, ry):
        return new_x
    else:
        return rx


rocks = [
    [[1, 1, 1, 1]],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [  # flipped
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]
cave = defaultdict(int)
gasses = open("d17.txt").read().strip()
seen = defaultdict(list)
step = 0

for i in range(3000):  # random number to get a cycle
    rock = rocks[i % len(rocks)]
    cx = 3
    cy = get_height(cave)

    while True:
        cx = blow(cave, rock, cx, cy)
        if no_collision(cave, rock, cx, cy - 1):
            cy -= 1
        else:
            break

    for y, row in enumerate(rock):
        for x, v in enumerate(row):
            if v == 1:
                cave[(cx + x, cy + y)] = v

    max_y = max([y for (_, y), v in cave.items() if v > 0])

    # period finding
    # rock no, gas step = round, height
    seen[(i % len(rocks), step % len(gasses))].append([i, max_y])

    if i == 2021:
        print(max_y)


goal = 1_000_000_000_000
cycle_slope = {}  # cycle increase
cycle_length = {}  # cycle duration
for k, v in seen.items():
    if len(v) > 1:
        cycle_slope[k] = (v[-1][1] - v[-2][1])
        cycle_length[k] = (v[-1][0] - v[-2][0])

        if (goal - v[0][0]) % cycle_length[k] == 0:
            break
    else:
        cycle_slope[k] = v[-1][1]

# dx/dy
slope = cycle_slope[k] / cycle_length[k]
intercept = seen[k][0][1] - slope * seen[k][0][0] - 1  # man i love off by 1

print(int(slope * goal + intercept))
