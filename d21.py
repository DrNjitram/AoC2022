from scipy.optimize import fsolve


def recurse(n, ops):
    return f"({''.join([str(v) if isinstance(v, int) or len(v) == 1 or v == 'humn' else recurse(v, ops) for v in ops[n]])})"


def reduce(yl, unk):
    reducing = True
    while reducing:
        reducing = False
        unk = {k: v for k, v in unk.items() if k not in yl}
        for name, (m1, m2, op) in unk.items():
            if m1 in yl and m2 in yl:
                reducing = True
                exec_str = f"{yl[m1]}{op}{yl[m2]}"
                result = int(eval(exec_str))
                yl[name] = result
    return yl, unk


def p1(yl, unk):
    print(reduce(yl, unk)[0]['root'])


def p2(yl, unk):
    yl.pop('humn')
    equals = unk.pop("root")[:2]

    yl, unk = reduce(yl, unk)

    ops = {name: (yl[m1] if m1 in yl else m1, op, yl[m2] if m2 in yl else m2) for name, (m1, m2, op) in unk.items()}

    goal = equals[1] if equals[0] in yl else equals[0]
    other = equals[0] if equals[0] in yl else equals[1]

    func = eval(f"lambda humn: {yl[other]}-{recurse(goal, ops)}")
    print(int(fsolve(func, 1000000)))


yells = {}
unknown = {}

monkeys = open("d21.txt").readlines()
for monkey in monkeys:
    name, yell = monkey.strip().split(": ")
    if " " in yell:
        m1, op, m2 = yell.split()
        unknown[name] = [m1, m2, op]
    else:
        yells[name] = int(yell)

p1(yells.copy(), unknown.copy())
p2(yells.copy(), unknown.copy())
