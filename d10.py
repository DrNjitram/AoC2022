cycles = [1]
pixels = []
cycle = 0

for command in open("d10.txt").readlines():
    cycle += 1
    cycles.append(cycles[-1])
    pixels.append("█" if abs((cycle - 1) % 40 - cycles[-1]) <= 1 else " ")

    if " " in command:
        cycle += 1
        pixels.append("█" if abs((cycle - 1) % 40 - cycles[-1]) <= 1 else " ")
        cycles.append(cycles[-1] + int(command.split()[1]))

for line in ["".join(pixels[i:i + 40]) for i in range(0, len(pixels), 40)]:
    print(line)

print(sum([cycles[c - 1] * c for c in [20 + i * 40 for i in range(6)]]))
