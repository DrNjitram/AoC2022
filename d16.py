from collections import defaultdict
from queue import PriorityQueue


def dijkstra(start_vertex, edges):
    D = [2 ** 32 - 1 for _ in range(len(edges))]
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    visited = []
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in edges[current_vertex]:
            if neighbor not in visited:
                if (new_cost := D[current_vertex] + 1) < D[neighbor]:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D


def search(k: int, minutes: int, pressure: int, elephant: bool):
    global checked
    pressure += minutes * flow_rate[k]
    best = pressure

    if all(checked):
        for tar in useful:
            if not checked[tar] and (d := distances[k][tar] + 1) < minutes:
                checked[tar] = True
                p = search(tar, minutes - d, pressure, elephant)
                best = max(best, p)

                if elephant:  # send in the elephant
                    p = pressure + ((minutes - d) * flow_rate[tar]) + search(aa_id, 26, 0, True)
                    best = max(best, p)

                checked[tar] = False

    return best


edges_id = []
flow_rate = []

valve_char = {}
aa_id = 0

for i, line in enumerate(open("d16.txt").readlines()):
    valve = line[6:8]
    valve_char[valve] = i
    if valve == 'AA':
        aa_id = i
    routes = [e[:2] for e in line.split()[9:]]
    flow_rate.append(int(line.split("=")[1].split(";")[0]))
    edges_id.append(routes)

edges = [[valve_char[c] for c in route] for route in edges_id]
distances = [dijkstra(start, edges) for start in range(len(edges_id))]

useful = [i for i, flow in enumerate(flow_rate) if flow > 0]

checked = defaultdict(bool)
ans1 = search(aa_id, 30, 0, False)
print(ans1)
ans2 = search(aa_id, 26, 0, True)
print(ans2)
