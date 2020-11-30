lines = open("temp.txt").readlines()

diffs = {}
for i in range(len(lines) - 1):
    if lines[i][0] == "-" and lines[i + 1][0] == "+":
        # print(lines[i].strip(), lines[i + 1].strip())
        type = None
        cw = None
        desc = None
        func = None
        for j in range(i, 0, -1):
            if "LANGNAME" in lines[j]:
                space = lines[j - 1].index(" ")
                type = lines[j - 1].split(" ")[1].strip()
                cw = lines[j - 1][space:].strip()
                space = cw.find(" ")
                cw = cw[space:].strip()
                desc = lines[j].split('"')[1].strip()
                func = lines[j + 1].split(" ")[2].strip()
                # mprint(lines[j - 1].strip(), lines[j].strip())
                break

        space = lines[i].index(" ")
        diff1 = lines[i][space:].strip()
        space = lines[i + 1].index(" ")
        diff2 = lines[i + 1][space:].strip()

        if type == "KENNFELD" or type == "KENNLINIE":
            diff1 = [float(x) for x in diff1.split(" ")]
            length = len(diff1)
            diff1 = [f"{num:.1f}" for num in diff1]
            diff1 = ", ".join(diff1)
            diff2 = [float(x) for x in diff2.split(" ")]
            diff2 = [f"{num:.1f}" for num in diff2]
            diff2 = ", ".join(diff2)

        if cw not in diffs:
            diffs[cw] = {"desc": None, "diffs": []}

        diffs[cw]["desc"] = desc
        diffs[cw]["diffs"].append((diff1, diff2))

        # print(f"{cw} ({func})")
        # print(desc)
        # print(f"{diff1} --> {diff2}")
        # print("------")

        print(type)


for cw in diffs:
    print(f"## {cw} ")
    print(f"### {diffs[cw]['desc']}")
    print("| Previous | New |")
    print("|----------|-----|")
    for diff in diffs[cw]["diffs"]:
        a, b = diff
        print(f"| {a} | {b} |")
    # print("|---|---|")
    print()