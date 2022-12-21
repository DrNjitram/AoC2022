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
    return tuple([l1[i] + l2[i] for i in range(len(l1))])


def subtract(l1, l2):
    return tuple([l1[i] - l2[i] for i in range(len(l2))] + [l1[3]])


def purchase_and_produce(stock: list, robots: list, purchase_index: int):
    stock_ = add(stock, robots)
    robots_ = list(robots)
    if purchase_index >= 0:
        robots_[purchase_index] += 1
        stock_ = subtract(stock_, costs[purchase_index])
    return stock_, tuple(robots_)


def produce_time(robot, stock, time_left):
    res = int(stock + (((robot + time_left) * ((robot + time_left) + 1)) / 2) - ((robot * (robot + 1)) / 2))
    return res


def iterate(bp: Type[Blueprint], robots=(1, 0, 0, 0), stock=(0, 0, 0, 0), time_left=24):
    global global_max

    if entry := (stock, robots, time_left) in seen:
        return seen[entry]

    if time_left == 0:
        global_max = max(stock[3], global_max)
        seen[entry] = stock[3]
        return stock[3]

    if produce_time(robots[3], stock[3], time_left) < global_max:
        seen[entry] = 0
        return 0

    if produce_time(robots[2], stock[2], time_left - 2) < bp.geode[2]:
        seen[entry] = stock[3] + robots[3] * time_left
        return stock[3] + robots[3] * time_left

    enough_robots = [robots[i] > ((max([rp[i] for rp in costs]) * time_left - stock[i]) // time_left) for i in
                     range(3)] + [False]
    resources = [all([cost[i] <= stock[i] for i in range(len(cost))]) for cost in costs]

    buyable = [resources[i] and not enough_robots[i] for i in range(4)]
    buyable[1] = buyable[1] and not enough_robots[2]  # only need clay if we need obsidian

    results = []  # results of this iteration
    if buyable[3]:
        stock_, robots_ = purchase_and_produce(stock, robots, 3)
        results.append(iterate(bp, robots_, stock_, time_left - 1))
    elif buyable[2]:
        stock_, robots_ = purchase_and_produce(stock, robots, 2)
        results.append(iterate(bp, robots_, stock_, time_left - 1))
    else:
        if buyable[1]:
            stock_, robots_ = purchase_and_produce(stock, robots, 1)
            results.append(iterate(bp, robots_, stock_, time_left - 1))
        if buyable[0]:
            stock_, robots_ = purchase_and_produce(stock, robots, 0)
            results.append(iterate(bp, robots_, stock_, time_left - 1))
        if not buyable[0] or (stock[1] and not enough_robots[2] or stock[2]):
            stock_, robots_ = purchase_and_produce(stock, robots, -1)
            results.append(iterate(bp, robots_, stock_, time_left - 1))

    score = max(results)
    seen[entry] = score
    return score


blueprints = []

p1 = 0
p2 = 1
for no, line in enumerate(open("d19.txt").readlines()):
    blueprint = Blueprint
    line = line.strip().split(": ")[1]
    for section in line[:-1].split("."):
        words = section.split()
        t = words[1]
        vals = [(words[-1 - 3 * i], words[-2 - 3 * i]) for i in range(1 + ((len(words) - 6) // 3))]
        exec(f"blueprint.{t} = get_costs(vals)")

    global_max = 0
    seen = {}
    costs = [blueprint.ore, blueprint.clay, blueprint.obsidian, blueprint.geode]
    geode = iterate(blueprint)
    print(f"BP {no+1}: {(no+1)*geode}")
    p1 += (no + 1) * geode

    if no < 3:
        global_max = 0
        seen = {}
        costs = [blueprint.ore, blueprint.clay, blueprint.obsidian, blueprint.geode]
        geode = iterate(blueprint, time_left=32)
        print(f"BP {no+1}: {geode}")
        p2 *= geode

print(p1)
print(p2)
