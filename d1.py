
def part1(line):
    elves = sorted([sum([int(val) for val in section.split("\n") if val != ""]) for section in line.split("\n\n")])

    print(elves[-1], sum(elves[-3:]))

part1(open("d1.txt").read())