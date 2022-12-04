s1 = lambda e1, e2: True if (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e2[0] >= e1[0] and e2[1] <= e1[1]) else False

s2 = lambda e1, e2: True if (e2[0] <= e1[0] <= e2[1]) or (e1[0] <= e2[0] <= e1[1]) else False

f = [[[int(s) for s in e.split("-")] for e in l.strip().split(',')] for l in open("d4.txt").readlines()]

print(sum([s1(p[0], p[1]) for p in f]), sum([s2(p[0], p[1]) for p in f]))
