



from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

    tlist = {}
    dup_count = 0
    biggest_x = 0
    biggest_y = 0
    for line in lines:
        rline = line.replace("->", "")
        cline = rline.split()

        x_start = int(cline[0].split(",")[0])
        y_start = int(cline[0].split(",")[1])
        x_end = int(cline[1].split(",")[0])
        y_end = int(cline[1].split(",")[1])


        if x_start > biggest_x:
            biggest_x = x_start
        if x_end > biggest_x:
            biggest_x = x_end
        if y_start > biggest_y:
            biggest_y = y_start
        if y_end > biggest_y:
            biggest_y = y_end


        if x_start != x_end and y_start != y_end:
            new_x_st = x_start
            new_x_en = x_end
            new_y_st = y_start
            new_y_en = y_end

            if new_x_st < new_x_en:
                new_x_en += 1
                incr_x = True
            else:
                new_x_en -= 1
                incr_x = False

            if new_y_st < new_y_en:
                new_y_en += 1
                incr_y = True
            else:
                new_y_en -= 1
                incr_y = False

            while new_x_st != new_x_en and new_y_st != new_y_en:
                tup_i = (new_x_st, new_y_st)

                if tup_i in tlist:
                    seen_twice = tlist[tup_i]
                    if not seen_twice:
                        tlist[tup_i] = True
                        dup_count += 1
                else:
                    tlist[tup_i] = False
                if incr_x:
                    new_x_st += 1
                else:
                    new_x_st -= 1

                if incr_y:
                    new_y_st += 1
                else:
                    new_y_st -= 1
        else:
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

    board = []
    for j in range(0, biggest_y + 1):
        row = []
        for i in range(0, biggest_x + 1):
            tup = (i,j)
            if tup in tlist:
                if tlist[tup]:
                    row.append("2")
                else:
                    row.append("1")
            else:
                row.append(".")
        board.append(row)

    import pdb;pdb.set_trace()
    print(dup_count)
