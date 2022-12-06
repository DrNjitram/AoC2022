import sys
sys.setrecursionlimit(2**12)


def check(chars: str, length: int):
    return len(chars) - length if len(set(chars[:length])) == length else check(chars[1:], length)


inp = open("d6.txt").readline().strip()
print(len(inp) - check(inp, 4))
print(len(inp) - check(inp, 14))
