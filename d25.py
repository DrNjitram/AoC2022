def snafu_to_decimal(snafu):
    SNAFU = 0
    val = 1
    for c in snafu[::-1]:
        if c == '-':
            SNAFU += -1 * val
        elif c == '=':
            SNAFU += -2 * val
        else:
            SNAFU += int(c) * val
        val *= 5
    return SNAFU


total = 0
for line in open("d25.txt").readlines():
    line = line.strip()
    total += snafu_to_decimal(line)


def decimal_to_snafu(dec) -> str:
    snafu = ''
    v = 5
    while dec:
        r = int(dec % v)
        if r < 3:
            snafu = str(r) + snafu
            dec = (dec - r) // v
        elif r == 3:
            snafu = '=' + snafu
            dec = (dec + 2) // v
        elif r == 4:
            snafu = '-' + snafu
            dec = (dec + 1) // v
    return snafu


print(decimal_to_snafu(total), total)
