def s1(E1, E2):
    return True if (E1[0] >= E2[0] and E1[1] <= E2[1]) or (E2[0] >= E1[0] and E2[1] <= E1[1]) else False


def s2(E1, E2):
    return True if (E2[0] <= E1[0] <= E2[1]) or (E1[0] <= E2[0] <= E1[1]) else False


inp = [[[int(section) for section in elf.split("-")] for elf in line.strip().split(',')] for line in open("d4.txt").readlines()]

print(sum([s1(p[0], p[1]) for p in inp]))
print(sum([s2(p[0], p[1]) for p in inp]))
