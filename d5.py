stack, moves = [s.split("\n") for s in open("d5.txt").read().split("\n\n")]

size = int(stack.pop()[-1])

stacks = [[] for _ in range(size)]

for line in stack[::-1]:
    for i in range(size):
        if len(line) > i * 4 and line[i * 4 + 1] != " ":
            stacks[i].append(line[i * 4 + 1])

part2 = [row[:] for row in stacks]

for move in moves:
    s, b, e = [int(move.split(" ")[i]) for i in [1, 3, 5]]
    stacks[e - 1].extend(stacks[b - 1][-s:][::-1])
    stacks[b - 1] = stacks[b - 1][:-s]

    part2[e - 1].extend(part2[b - 1][-s:])
    part2[b - 1] = part2[b - 1][:-s]

print("".join([s.pop() for s in stacks]), "".join([s.pop() for s in part2]))
