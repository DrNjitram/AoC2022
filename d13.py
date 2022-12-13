import ast
import functools
import itertools


def order(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if type(left[i]) == type(right[i]) == int:
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
            else:
                i += 1
        elif type(left[i]) == type(right[i]) == list:
            cmp = order(left[i], right[i])
            if cmp is not None: return cmp
            if len(left[i]) < len(right[i]):
                return True
            elif len(left[i]) > len(right[i]):
                return False
            else:
                i += 1
        else:
            if type(left[i]) == int:
                cmp = order([left[i]], right[i])
                if cmp is not None: return cmp
            else:
                cmp = order(left[i], [right[i]])
                if cmp is not None: return cmp
            i += 1

    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return None


pairs = [[ast.literal_eval(packet) for packet in p.split("\n")] for p in open("d13.txt").read().split("\n\n")]

count = sum([i + 1 for i, (left, right) in enumerate(pairs) if order(left, right)])

pairs = list(itertools.chain(*pairs))
pairs.extend([[[2]], [[6]]])

pairs = sorted(pairs, key=functools.cmp_to_key(lambda x, y: -1 if order(x, y) else 1))

print(count)
print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))
