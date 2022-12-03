def conv(c): return ord(c) - 96 if c >= 'a' else ord(c) - 38


def prio1(b): return conv((set(b[:len(b) // 2]) & set(b[len(b) // 2:])).pop())


def prio2(b): return conv((set(b[0]) & set(b[1]) & set(b[2])).pop())


elves = [l.strip() for l in open('d3.txt').readlines()]

print(sum([prio1(bp) for bp in elves]))
print(sum([prio2(elves[i:i + 3]) for i in range(0, len(elves), 3)]))