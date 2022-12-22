from collections import namedtuple
from itertools import combinations

Valve = namedtuple("Valve", ("name", "rate", "destinations"))

valves = {}
shortest_paths = {}

def explore(start: Valve, unvisited, turns=0, rate=0, flow=0, path=None, max_turns=30, paths=None):
    if len(unvisited) == 0:
        flow += (max_turns - turns) * rate
        paths.append((path, flow))
        return flow
    for v in unvisited:
        # travel then open valve
        new_turns = shortest_paths.get(key(start.name, v.name), 0) + 1
        if new_turns == 1 or turns + new_turns > max_turns:
            new_flow = (max_turns - turns) * rate
            paths.append((path, flow + new_flow))
            continue
        new_flow = rate * new_turns
        explore(v, unvisited=unvisited - {v}, turns=turns + new_turns, rate=rate + v.rate, flow=flow+new_flow, path=path + [v.name], max_turns=max_turns, paths=paths)

def key(a, b):
    return tuple(sorted([a, b]))

def best(paths):
    max_flow = (None, 0)
    for p in paths:
        if p[1] > max_flow[1]:
            max_flow = p
    return max_flow

def main():
    with open("d16.txt") as fh:
        lines = [line.strip() for line in fh.readlines()]
    for line in lines:
        v, t = line.split("; ")
        s = v.split()[1]
        r = int(v.split("=")[1])
        t = [d[:2] for d in t.split()[4:]]
        for d in t:
            shortest_paths[key(s, d)] = 1
            new_paths = {}
            for p, l in shortest_paths.items():
                if d == p[0] and p[1] != s:
                    k = key(p[1], s)
                elif d == p[1] and p[0] != s:
                    k = key(p[0], s)
                else:
                    continue
                if k not in shortest_paths or l + 1 < shortest_paths[k]:
                    new_paths[k] = l + 1
            shortest_paths.update(new_paths)
        valves[s] = Valve(s, r, tuple(t))
    unvisited = {v for v in valves.values() if v.rate != 0}
    paths = []
    explore(valves["AA"], unvisited=unvisited, path=[], max_turns=30, paths=paths)
    print("part 1", best(paths))

    max_flow = (None, None, 0)
    for i in range(len(valves)):
        for c in combinations(unvisited, i):
            s1 = set(c)
            s2 = unvisited - s1
            paths = []
            explore(valves["AA"], unvisited=s1, path=[], max_turns=26, paths=paths)
            b1 = best(paths)
            paths = []
            explore(valves["AA"], unvisited=s2, path=[], max_turns=26, paths=paths)
            b2 = best(paths)
            if b1[1] + b2[1] > max_flow[2]:
                max_flow = (b1, b2, b1[1] + b2[1])
    print("part 2", max_flow)

main()