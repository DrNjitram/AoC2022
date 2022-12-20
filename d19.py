from typing import NamedTuple, Type

# Cost: [ore, clay, obsidian, geode]
Blueprint = NamedTuple("Blueprint", ore=list, clay=list, obsidian=list, geode=list, index=int, geode_yield=int)
types = {0: "Ore", 1: "Clay", 2: "Obsidian", 3: "Geode"}


def get_costs(cs):
    costs = [0, 0, 0]
    for t, c in cs:
        costs[{"ore": 0, "clay": 1, "obsidian": 2}[t]] = int(c)
    return costs


def add(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]


def intermediate(bp: Type[Blueprint], robots: list, stock: list, minute_max: int, minute: int,
                 purchase: int, previous: list):
    stock = add(stock, robots)
    costs = [bp.ore, bp.clay, bp.obsidian, bp.geode]
    if purchase > -1:
        robots[purchase] += 1
        for i in range(3):
            stock[i] -= costs[purchase][i]

    return iterate(bp, robots, stock, minute_max, minute, previous)


def iterate(bp: Type[Blueprint], robots: list, stock: list, minute_max: int, minute: int,
            previous: list):
    global global_max

    if stock[3] > global_max[0] and minute <= global_max[1]:
        global_max = (stock[3], minute)

    if minute == minute_max or (stock[3] < global_max[0] and minute >= global_max[1]):
        return global_max[0]

    costs = [bp.ore, bp.clay, bp.obsidian, bp.geode]

    buyable = [all([cost[i] <= stock[i] for i in range(len(cost))]) for cost in costs]
    enough = [robots[i] > max([rp[i] for rp in costs]) for i in range(3)] + [False]
    buyable = [buyable[i] and not previous[i] and not enough[i] for i in range(4)]

    if any(buyable):
        if buyable[3]:
            return intermediate(bp, robots, stock, minute_max, minute + 1, 3, buyable)
        else:
            return max(
                [intermediate(bp, robots, stock, minute_max, minute + 1, i, buyable) for i in range(3) if buyable[i]])

    stock = add(stock, robots)

    return iterate(bp, robots, stock, minute_max, minute + 1, buyable)


for line in open("d19_test.txt").readlines():
    bp = Blueprint
    line = line.strip().split(": ")[1]
    for section in line[:-1].split("."):
        words = section.split()
        t = words[1]
        costs = [(words[-1 - 3 * i], words[-2 - 3 * i]) for i in range(1 + ((len(words) - 6) // 3))]
        exec(f"bp.{t} = get_costs(costs)")

    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

    global_max = (0, 24) # geode, minute
    geode = iterate(bp, [1, 0, 0, 0],  [0, 0, 0, 0], 24, 0, [False, False, False, False])
    print(geode)

