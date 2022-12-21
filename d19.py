from typing import NamedTuple, Type

# Cost: [ore, clay, obsidian, geode]
Blueprint = NamedTuple("Blueprint", ore=list, clay=list, obsidian=list, geode=list, index=int, geode_yield=int)
types = {0: "Ore", 1: "Clay", 2: "Obsidian", 3: "Geode"}


def get_costs(cs):
    csts = [0, 0, 0]
    for tp, c in cs:
        csts[{"ore": 0, "clay": 1, "obsidian": 2}[tp]] = int(c)
    return csts


def add(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]


def produce_time(robot, stock, time_left):
    res = int(stock + (((robot + time_left) * ((robot + time_left) + 1)) / 2) - ((robot * (robot + 1)) / 2))
    return res


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
        global_max = [stock[3], minute, global_max[2]]

    if (a := (produce_time(robots[2], stock[2], minute_max - minute - 2) < bp.geode[2])) \
            or (b := (minute == minute_max)) \
            or (c := (stock[3] < global_max[0] and minute >= global_max[1])) \
            or (d := (produce_time(robots[3], stock[3], minute_max - minute - 1) < global_max[2])):
        # timeout
        # behind best,
        # cant ever produce another geode
        # cant ever produce enough geodes
        if a and stock[3] > 0:
            stock[3] = stock[3] + robots[3] * (minute_max - minute)
        global_max[2] = max(stock[3], global_max[2])
        return global_max[2]

    costs = [bp.ore, bp.clay, bp.obsidian, bp.geode]

    resources = [all([cost[i] <= stock[i] for i in range(len(cost))]) for cost in costs]
    enough = [robots[i] > max([rp[i] for rp in costs]) for i in range(3)] + [False]
    buyable = [resources[i] and not previous[i] and not enough[i] for i in range(4)]

    if any(buyable):
        if buyable[3]:
            return intermediate(bp, robots[:], stock[:], minute_max, minute + 1, 3, buyable[:])
        elif buyable[2] and robots[2] == 0:
            return intermediate(bp, robots[:], stock[:], minute_max, minute + 1, 2, buyable[:])
        elif buyable[1] and robots[1] == 0:
            return intermediate(bp, robots[:], stock[:], minute_max, minute + 1, 1, buyable[:])
        else:
            min_range = -1 if buyable[1] and robots[1] == 0 else -2
            return max(
                [intermediate(bp, robots[:], stock[:], minute_max, minute + 1, i, buyable[:]) for i in
                 range(3, min_range, -1) if
                 (buyable[i] or i == -1)]
            )
    else:
        stock = add(stock, robots)

        return iterate(bp, robots[:], stock[:], minute_max, minute + 1, buyable[:])


for no, line in enumerate(open("d19_test.txt").readlines()[1:]):
    blueprint = Blueprint
    line = line.strip().split(": ")[1]
    for section in line[:-1].split("."):
        words = section.split()
        t = words[1]
        vals = [(words[-1 - 3 * i], words[-2 - 3 * i]) for i in range(1 + ((len(words) - 6) // 3))]
        exec(f"blueprint.{t} = get_costs(vals)")

    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
    # Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.

    global_max = [0, 24, 0]  # geode at minute, total max
    geode = iterate(blueprint, [1, 0, 0, 0], [0, 0, 0, 0], 24, 0, [False, False, False, False])
    print(no, geode)
