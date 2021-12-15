from collections import defaultdict
from copy import copy




def gen_new_lines(lines, index, reverse=False,):
    tmp = defaultdict(list)
    one_count = 0
    zero_count = 0
    for line in lines:
        l_ent = line[index]
        tmp[l_ent].append(line)
        if l_ent == "1":
            one_count += 1
        else:
            zero_count += 1

    if one_count == zero_count:
        if reverse:
            new_lines = tmp["0"]
        else:
            new_lines = tmp["1"]
    elif one_count > zero_count:
        if reverse:
            new_lines = tmp["0"]
        else:
            new_lines = tmp["1"]

    elif zero_count > one_count:
        if reverse:
            new_lines = tmp["1"]
        else:
            new_lines = tmp["0"]

    return new_lines

with open("input1.txt") as f:
    lines = f.readlines()
    new_lines = [line.rstrip() for line in lines]

    cval = None
    index = 0
    lines = copy(new_lines)
    while cval is None:
        lines = gen_new_lines(lines, index)
        index+= 1
        if len(lines) == 1:
            cval = lines[0]

    sval = None
    index = 0
    lines = copy(new_lines)

    while sval is None:
        lines = gen_new_lines(lines, index, reverse=True)
        index += 1
        if len(lines) == 1:
            sval = lines[0]

    c_val = int(cval, 2)
    s_val = int(sval, 2)
    import pdb;pdb.set_trace()
