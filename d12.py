from collections import defaultdict
from queue import PriorityQueue

heightmap = [l.strip() for l in open("d12.txt").readlines()]

start = [(heightmap[y].index("S"), y) for y in range(len(heightmap)) if 'S' in heightmap[y]][0]
end = [(heightmap[y].index("E"), y) for y in range(len(heightmap)) if 'E' in heightmap[y]][0]


def get_passability(cur_pos, neigh):
    cur = heightmap[cur_pos[1]][cur_pos[0]]

    target = heightmap[neigh[1]][neigh[0]]

    cur = 'a' if cur == 'S' else cur
    target = 'z' if target == 'E' else target

    return True if ord(target) - ord(cur) <= 1 else False


def dijkstra(start):
    D = defaultdict(lambda: float('inf'))
    D[start] = 0

    visited = []

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, curr) = pq.get()
        visited.append(curr)

        for neighbor in [(curr[0] + n[0], curr[1] + n[1]) for n in [[0, 1], [1, 0], [-1, 0], [0, -1]] if
                         0 <= curr[0] + n[0] < len(heightmap[0]) and 0 <= curr[1] + n[1] < len(heightmap)]:
            if get_passability(curr, neighbor):
                if neighbor not in visited and (new_cost := D[curr] + 1) < D[neighbor]:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
                    if neighbor == end:
                        break
    return D


path = dijkstra(start)
print(path[end])

dists = []
for target in [[(x,y) for x in range(len(heightmap[0])) if heightmap[y][x] == 'a'] for y in range(len(heightmap))]:
    for t in target:
        dists.append(dijkstra(t)[end])

print(min(dists))
