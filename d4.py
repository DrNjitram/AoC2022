s1 = lambda e1, e2: True if (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e2[0] >= e1[0] and e2[1] <= e1[1]) else False

s2 = lambda e1, e2: True if (e2[0] <= e1[0] <= e2[1]) or (e1[0] <= e2[0] <= e1[1]) else False

f = [[[int(s) for s in e.split("-")] for e in l.strip().split(',')] for l in open("d4.txt").readlines()]

print(sum([s1(p[0], p[1]) for p in f]), sum([s2(p[0], p[1]) for p in f]))

#One liner filth
print([sum(lst) for lst in [[[[True if (p[0][0] >= p[1][0] and p[0][1] <= p[1][1]) or (p[1][0] >= p[0][0] and p[1][1] <= p[0][1]) else False for p in f], [True if (p[1][0] <= p[0][0] <= p[1][1]) or (p[0][0] <= p[1][0] <= p[0][1]) else False for p in f]]] for f in [[[[int(s) for s in e.split("-")] for e in l.strip().split(',')] for l in open("d4.txt").readlines()]]][0][0]])