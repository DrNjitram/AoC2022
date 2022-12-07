from collections import defaultdict
import json
# dir : {contents}
files = []
folders = defaultdict(int)
cur_dir = "."

for block in open("d7.txt").read().split("$ ")[1:]:
    lines = [line for line in block.split("\n") if line != ""]

    if lines[0].startswith("cd"):
        folder = lines[0].split(" ")[1]
        match folder:
            case "/":
                cur_dir = "./"
            case "..":
                cur_dir = "/".join(cur_dir.split("/")[:-1])
            case _:
                cur_dir += f"/{folder}"
    else:
        for elem in lines[1:]:
            if not elem.startswith("dir"):
                size, f = elem.split(" ")
                files.append(f"{cur_dir}/{size}")


def recurse(lst: list) -> dict:
    tmp = {}
    done = []

    for elem in lst:
        if "/" in elem:  # subfolder
            subpath = elem.split("/")[0] + "/"
            if subpath not in done:
                done.append(subpath)
                tmp[subpath[:-1]] = recurse([p[len(subpath):] for p in lst if p.startswith(subpath)])
        else:  # file
            if "files" not in tmp:
                tmp["files"] = int(elem)
            else:
                tmp["files"] += int(elem)

    return tmp


answer = 0
sizes = []


def collect(d: dict):
    global answer, sizes
    s = 0
    for key, value in d.items():
        if type(value) == int:
            s += value
        else:
            s += collect(value)
    d["total"] = s
    if s < 100000:
        answer += s
    sizes.append(s)
    return s


start_path = "./"
nest = recurse([p[len(start_path):] for p in files if p.startswith(start_path)])
collect(nest)

print(answer)
print(min([size for size in sizes if 70000000 - nest["total"] + size > 30000000]))
