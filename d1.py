

def part1(lines):
    elves = []

    buffer = 0
    for line in lines:
        if line.strip() == "":
            elves.append(buffer)
            buffer = 0
        else:
            buffer += int(line)
    elves.append(buffer)

    print(max(elves))

    print(sum(sorted(elves)[-3:]))

part1("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000".split("\n"))

file = open("d1.txt").readlines()
part1(file)