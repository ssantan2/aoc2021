

with open("prob1_input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    val = 0
    last_pos = None
    tot_len = len(lines)


    new_lines = []
    for index, value in enumerate(lines):
        for sub_index in range(1,3):
            nub_index = index - sub_index
            if nub_index < 0:
                continue
            new_lines[nub_index] += int(value)

        # add new line
        new_lines.append(int(value))



    for line in new_lines:
        if last_pos is not None and line > last_pos:
            val += 1
        last_pos = line

    print(val)


