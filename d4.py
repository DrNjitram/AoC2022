s1 = lambda e1, e2: (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e2[0] >= e1[0] and e2[1] <= e1[1])

s2 = lambda e1, e2:  (e2[0] <= e1[0] <= e2[1]) or (e1[0] <= e2[0] <= e1[1])

f = [[[int(s) for s in e.split("-")] for e in l.strip().split(',')] for l in open("d4.txt").readlines()]

print(sum([s1(p[0], p[1]) for p in f]), sum([s2(p[0], p[1]) for p in f]))

# One-liner filth
print(list(map(sum, list(map(lambda f: [list(map(lambda p:  (p[0][0] >= p[1][0] and p[0][1] <= p[1][1]) or (p[1][0] >= p[0][0] and p[1][1] <= p[0][1]), f)),list(map(lambda p: (p[1][0] <= p[0][0] <= p[1][1]) or (p[0][0] <= p[1][0] <= p[0][1]), f))],[list(map(lambda l: list(map(lambda e: list(map(int, e.split("-"))), l.strip().split(','))), open("d4.txt").readlines()))]))[0])))
