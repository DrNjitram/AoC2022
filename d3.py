def conv(c): return ord(c) - 96 if c >= 'a' else ord(c) - 38

elves = [l.strip() for l in open('d3.txt').readlines()]

print(sum([conv((set(b[:len(b) // 2]) & set(b[len(b) // 2:])).pop()) for b in elves]))
print(sum([conv((set(elves[i]) & set(elves[i+1]) & set(elves[i+2])).pop()) for i in range(0, len(elves), 3)]))
