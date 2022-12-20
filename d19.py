from typing import NamedTuple


def get_costs(cs):
    costs = [0, 0, 0]
    for t, c in cs:
        costs[{"ore": 0, "clay": 1, "obsidian": 2}[t]] = int(c)
    return costs


def add(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]


# Cost: [ore, clay, obsidian, geode]
Blueprint = NamedTuple("Blueprint", ore=list, clay=list, obsidian=list, geode=list, index=int, geode_yield=int)
types = {0: "Ore", 1: "Clay", 2: "Obsidian", 3: "Geode"}

for line in open("d19_test.txt").readlines()[1:]:
    bp = Blueprint
    line = line.strip().split(": ")[1]
    for section in line[:-1].split("."):
        words = section.split()
        t = words[1]
        costs = [(words[-1 - 3 * i], words[-2 - 3 * i]) for i in range(1 + ((len(words) - 6) // 3))]
        exec(f"bp.{t} = get_costs(costs)")

    # Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.

    # ore, clay, obsidian, geode
    robots = [1, 0, 0, 0]
    stock = [0, 0, 0, 0]
    prod_ratio_target = []
    costs = [bp.ore, bp.clay, bp.obsidian, bp.geode]
    print(costs)
    minutes = 1

    while minutes < 25:
        purchase = -1
        buyable = [all([cost[i] <= stock[i] for i in range(len(cost))]) for cost in costs]
        if any(buyable):
            if bp.geode[0] - stock[0] <= robots[0] * 2 and bp.geode[2] - stock[2] <= robots[2] * 2:
                if buyable[3]:  # Geode
                    purchase = 3
            elif bp.obsidian[0] - stock[0] <= robots[0] * 2 and bp.obsidian[1] - stock[1] <= robots[1] * 2:
                if buyable[2]:
                    purchase = 2
            else:
                if buyable[2] and (bp.geode[2] / bp.geode[0] > robots[2] / robots[0] or robots[2] == 0):  # Obsidian
                    purchase = 2
                elif buyable[1] and (
                        (bp.obsidian[1]) / bp.obsidian[0] > robots[1] / robots[0] or robots[1] == 0):  # Clay
                    purchase = 1
                elif buyable[0] and not (
                        bp.geode[2] / bp.geode[0] > robots[2] / robots[0] or bp.obsidian[1] / bp.obsidian[0] > robots[
                    1] /
                        robots[0]) \
                        and bp.geode[0] - stock[0] < 2:  # Ore
                    purchase = 0

        stock = add(stock, robots)

        if purchase > -1:
            print(f"Bought {types[purchase]} at {minutes} min")
            robots[purchase] += 1
            for i in range(3):
                stock[i] -= costs[purchase][i]

        print(f"Minute {minutes}:  robots: {robots}, stock: {stock}")
        minutes += 1

    print(robots)
    print(stock)
