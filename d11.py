import math
from copy import deepcopy

monkeys = []
held = []

for monkey in [m.split("\n") for m in open("d11.txt").read().split("\n\n")]:
    items = list(map(int, monkey[1].split(":")[1].split(",")))

    if '+' in monkey[2]:
        operation = eval(f"lambda old: (old + {int(monkey[2].split()[-1])})")
    elif '* old' in monkey[2]:
        operation = lambda old: old ** 2
    else:
        operation = eval(f"lambda old: (old * {int(monkey[2].split()[-1])})")

    test = int(monkey[3].split("by")[1])
    t_true = int(monkey[4].split("monkey")[1])
    t_false = int(monkey[5].split("monkey")[1])

    held.append(items)
    monkeys.append([operation, test, t_true, t_false])


def p2(held, const):
    handled = [0 for _ in range(len(monkeys))]
    for _ in range(10000):
        for i, (op, test, true, false) in enumerate(monkeys):
            curr = held[i]
            held[i] = []
            for item in curr:
                item = op(item) % const

                held[false if item % test else true].append(item)
                handled[i] += 1

    hs = sorted(handled)
    print(hs[-1] * hs[-2])


def p1(held):
    handled = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for i, (op, test, true, false) in enumerate(monkeys):
            curr = held[i]
            held[i] = []
            for item in curr:
                item = op(item) // 3

                held[false if item % test else true].append(item)
                handled[i] += 1

    hs = sorted(handled)
    print(hs[-1] * hs[-2])


p1(deepcopy(held))
p2(held, math.prod([m[1] for m in monkeys]))
