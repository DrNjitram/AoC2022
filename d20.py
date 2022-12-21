def mix(lst, no=1):
    sub = [i for i in range(len(lst))]
    og = sub.copy()

    for _ in range(no):
        for val in og:
            i = sub.index(val)
            sub_i = sub.pop(i)
            v = lst[sub_i]
            sub.insert((i + v) % (len(sub)), sub_i)

    return sub


d = [int(i) for i in open("d20.txt").readlines()]

mixed = mix(d)
mixed = [d[v] for v in mixed]

print(sum([mixed[(mixed.index(0) + i) % len(mixed)] for i in [1000, 2000, 3000]]))

d = [v * 811589153 for v in d]

mixed = mix(d, 10)
mixed = [d[v] for v in mixed]

print(sum([mixed[(mixed.index(0) + i) % len(mixed)] for i in [1000, 2000, 3000]]))
