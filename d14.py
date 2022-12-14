from collections import defaultdict
from numpy import linspace


def print_map(cave_map):  # disgusting please ignore
    [print("".join([{0: ".", 1: "#", 2: "o", 3: "+"}[cave_map[(x, y)]] for x in range(min([p[0] for p in cave_map.keys()]), max([p[0] for p in cave_map.keys()]) + 1)])) for y in range(min([p[1] for p in cave_map.keys()]), max([p[1] for p in cave_map.keys()]) + 1)]


cave = defaultdict(int)

for points in [[[int(p) for p in pair.split(",")] for pair in trace.strip().split(" -> ")] for trace in
               open("d14.txt").readlines()]:
    for i in range(len(points) - 1):
        for x in linspace(points[i][0], points[i + 1][0], abs(points[i + 1][0] - points[i][0]) + 1):
            for y in linspace(points[i][1], points[i + 1][1], abs(points[i + 1][1] - points[i][1]) + 1):
                cave[(int(x), int(y))] = 1

# print_map(cave)
bottom = max([p[1] for p in cave.keys()]) + 2

for x in linspace(-bottom + 500, bottom + 500, int(2 * bottom + 1)):  # right angled triangles bby
    cave[(int(x), bottom)] = 1

p1 = 0
while True:
    sand = [500, 0]
    can_move = True
    while can_move:
        can_move = False
        for next_p in [[sand[0] + i[0], sand[1] + i[1]] for i in [[0, 1], [-1, 1], [1, 1]]]:
            if cave[tuple(next_p)] == 0:
                can_move = True
                sand = next_p
                break

    cave[tuple(sand)] = 2
    if sand[1] > bottom - 2 and not p1:
        p1 = list(cave.values()).count(2) - 1  # Do not count last placed grain
    if sand == [500, 0]:
        break

# print_map(cave)
print(f"Part 1: {p1}")
print(f"Part 2: {list(cave.values()).count(2)}")
