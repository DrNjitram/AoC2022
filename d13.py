import functools
import itertools


def order(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if type(left[i]) is type(right[i]) is int:
            if left[i] == right[i]:
                i += 1
            else:
                return left[i] < right[i]
        elif type(left[i]) is type(right[i]) is list:
            cmp = order(left[i], right[i])
            if cmp is not None:
                return cmp
            if len(left[i]) == len(right[i]):
                i += 1
            else:
                return len(left[i]) < len(right[i])
        else:
            if type(left[i]) is int:
                cmp = order([left[i]], right[i])
            else:
                cmp = order(left[i], [right[i]])
            if cmp is not None:
                return cmp
            i += 1

    if len(left) == len(right):
        return None
    else:
        return len(left) < len(right)


pairs = [[eval(packet) for packet in p.split("\n")] for p in open("d13.txt").read().split("\n\n")]

count = sum([i + 1 for i, (left, right) in enumerate(pairs) if order(left, right)])

pairs = sorted(list(itertools.chain(*pairs)) + [[[2]], [[6]]],
               key=functools.cmp_to_key(lambda x, y: -1 if order(x, y) else 1))

print(count)
print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))
