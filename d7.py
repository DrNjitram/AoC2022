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
            tmp["files"] = int(elem) + tmp.get("files", 0)

    return tmp


def collect(d: dict) -> int:
    global sizes
    s = 0
    for key, value in d.items():
        if type(value) == int:
            s += value
        else:
            s += collect(value)
    d["total"] = s
    sizes.append(s)
    return s


files = []
cur_dir = "."
sizes = []

for block in open("d7.txt").read().split("$ ")[1:]:
    lines = [line.strip() for line in block.split("\n") if line != ""]

    if lines[0].startswith("cd"):
        folder = lines[0].split(" ")[1]
        match folder:
            case "/":
                cur_dir = "./"
            case "..":
                cur_dir = cur_dir[:cur_dir.rfind("/")]
            case _:
                cur_dir += f"/{folder}"
    else:
        for elem in lines[1:]:
            if not elem.startswith("dir"):
                size, f = elem.split(" ")
                files.append(f"{cur_dir}/{size}")


start_path = "./"
nest = recurse([p[len(start_path):] for p in files if p.startswith(start_path)])
collect(nest)

print(sum([size for size in sizes if size < 100000]))
print(min([size for size in sizes if 40000000 - nest["total"] + size > 0]))
