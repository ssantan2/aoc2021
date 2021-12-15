



from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

    tlist = {}
    dup_count = 0

    for line in lines:
        rline = line.replace("->", "")
        cline = rline.split()

        x_start = int(cline[0].split(",")[0])
        y_start = int(cline[0].split(",")[1])
        x_end = int(cline[1].split(",")[0])
        y_end = int(cline[1].split(",")[1])


        if x_start != x_end and y_start != y_end:
            continue
        if x_start > x_end:
            tmp = x_start
            x_start = x_end
            x_end = tmp

        if y_start > y_end:
            tmp = y_start
            y_start = y_end
            y_end = tmp

        for i in range(x_start, x_end+1):
            for j in range(y_start, y_end+1):
                tup_i = (i,j)
                if tup_i in tlist:
                    seen_twice = tlist[tup_i]
                    if not seen_twice:
                        tlist[tup_i] = True
                        dup_count += 1
                else:
                    tlist[tup_i] = False

    print(dup_count)
