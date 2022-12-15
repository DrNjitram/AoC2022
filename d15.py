import re


def get_data(line):
    match = re.search(r"Sensor at x=([\-0-9]+), y=([\-0-9]+): closest beacon is at x=([\-0-9]+), y=([\-0-9]+)", line)
    data = list(map(int, [match.group(1), match.group(2), match.group(3), match.group(4)]))
    return data + [abs(data[0] - data[2]) + (abs(data[1] - data[3]))]


def part2(high):
    y = 0
    while y < high:
        x = 0
        while x < high:
            found = False
            for sx, sy, bx, by, manhattan in sensors:
                if abs(x - sx) + abs(y - sy) <= manhattan:
                    found = True
                    if x < sx:
                        x = sx + manhattan - abs(y - sy)
                    else:
                        x += manhattan - abs(y - sy)
                    break
            if not found:
                return x, y
            x += 1
        y += 1


f = "d15.txt"
sensors = [get_data(line) for line in open(f).readlines()]

cave = {}

possible = 0

for sx, sy, bx, by, manhattan in sensors:
    cave[(sx, sy)] = 1
    cave[(bx, by)] = 2

y = 10 if 'test' in f else 2000000
for x in range(int(min([s[0] - s[4] for s in sensors]) - 1), int(max([s[0] + s[4] for s in sensors]) + 2)):
    if (x, y) in cave:
        continue
    for sx, sy, bx, by, manhattan in sensors:
        if abs(x - sx) + abs(y - sy) <= manhattan:
            possible += 1
            break

print(possible)

x, y = part2(20 if 'test' in f else 4000000)
print(x * 4000000 + y)
