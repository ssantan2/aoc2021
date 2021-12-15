from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()
    fish_arr = [int(num) for num in lines[0].split(",")]

    days = 256
    fish_dict = defaultdict(int)
    # pop initial dict
    for fish in fish_arr:
        fish_dict[fish] += 1
    while days > 0:
        day_zeros = fish_dict[0]
        fish_dict[0] = fish_dict[1]
        fish_dict[1] = fish_dict[2]
        fish_dict[2] = fish_dict[3]
        fish_dict[3] = fish_dict[4]
        fish_dict[4] = fish_dict[5]
        fish_dict[5] = fish_dict[6]
        fish_dict[6] = fish_dict[7] + day_zeros
        fish_dict[7] = fish_dict[8]
        fish_dict[8] = day_zeros

        days -= 1

    fish_count = sum(list(fish_dict.values()))
    print(fish_count)
