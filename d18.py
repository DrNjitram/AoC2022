from collections import defaultdict
from queue import PriorityQueue


def in_range(point):
    return range_x[0] <= point[0] <= range_x[1] and range_y[0] <= point[1] <= range_y[1] and range_z[0] <= point[2] <= \
        range_z[1]


def dijkstra(start):
    D = defaultdict(lambda: 2 ** 32 - 1)
    D[start] = 0

    visited = []

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, curr) = pq.get()
        visited.append(curr)
        if curr in cache:
            return cache[curr]
        for neighbor in [(curr[0] + n[0], curr[1] + n[1], curr[2] + n[2]) for n in sides]:
            if neighbor not in drops and in_range(neighbor):
                if neighbor not in visited and (new_cost := D[curr] + 1) < D[neighbor]:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost

    return D


drops = [tuple(map(int, l.strip().split(','))) for l in open("d18.txt").readlines()]

sides = [
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

exposed = 0
for x, y, z in drops:
    for dx, dy, dz in sides:
        if (x + dx, y + dy, z + dz) not in drops:
            exposed += 1

print(exposed)

vals = list(zip(*drops))
range_x = [min(vals[0]) - 1, max(vals[0]) + 1]
range_y = [min(vals[1]) - 1, max(vals[1]) + 1]
range_z = [min(vals[2]) - 1, max(vals[2]) + 1]

exposed = 0
cache = defaultdict(bool)

outside = dijkstra((0, 0, 0))
for k, v in outside.items():
    if v < 2 ** 32 - 1:
        cache[k] = True

for (x, y, z) in drops:
    for dx, dy, dz in sides:
        neighbour = (x + dx, y + dy, z + dz)
        if neighbour not in drops and cache[neighbour]:
            exposed += 1

print(exposed)
