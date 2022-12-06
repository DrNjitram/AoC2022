s1 = {
    "A X": 4, "B X": 1, "C X": 7,
    "A Y": 8, "B Y": 5, "C Y": 2,
    "A Z": 3, "B Z": 9, "C Z": 6
}

s2 = {
    "A X": 3, "B X": 1, "C X": 2,
    "A Y": 4, "B Y": 5, "C Y": 6,
    "A Z": 8, "B Z": 9, "C Z": 7
}

def strategize(lines):
    return sum([s1[line.strip()] for line in lines]), sum([s2[line.strip()] for line in lines])


print(strategize(["A Y", "B X", "C Z"]))
print(strategize(open("d2.txt").readlines()))