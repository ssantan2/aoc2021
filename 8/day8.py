
# 1,4,7,8 are prime
# 0 =
#
#
#
#
#


with open("input.txt") as f:
    lines =f.readlines()
    uni_sets = [tuple(line.split("|")) for line in lines]


    uni_count = 0
    for char_list, other_list in uni_sets:
        # Find the set of characters for 1, 4, 7, 8
        char_list = char_list.split()
        other_list = other_list.split()

        char_map = {}
        for char in char_list:
            if len(char)  == 2:
                char_map[1] = set(char)
                char_map[tuple(sorted(char))] = "1"
            elif len(char)  == 4:
                char_map[4] = set(char)
                char_map[tuple(sorted(char))] = "4"
            elif len(char)  == 3:
                char_map[7] = set(char)
                char_map[tuple(sorted(char))] = "7"
            elif len(char)  == 7:
                char_map[8] = set(char)
                char_map[tuple(sorted(char))] = "8"


        # figure out the rest
        for char in char_list:
            char_set = set(char)
            if tuple(sorted(char)) in char_map:
                continue

            if (
                (char_map[7] | char_set) == char_set and
                (char_map[4] | char_set) != char_set and
                len(char_map[8] - char_set) == 1
            ):
                char_map[0] = char_set
                char_map[tuple(sorted(char))] = "0"
            elif len(char_set - char_map[4]) == 3 and  len(char_set - char_map[7]) == 3:
                char_map[2] = char_set
                char_map[tuple(sorted(char))] = "2"
            elif len(char_set - char_map[1]) == 3:
                char_map[3] = char_set
                char_map[tuple(sorted(char))] = "3"
            elif len(char_set) == 5:
                char_map[5] = char_set
                char_map[tuple(sorted(char))] = "5"
            elif char_set | char_map[7] != char_set:
                char_map[6] = char_set
                char_map[tuple(sorted(char))] = "6"
            else:
                char_map[9] = char_set
                char_map[tuple(sorted(char))] = "9"

        num_word = ""
        for ele in other_list:
            num_word += char_map[tuple(sorted(ele))]

        uni_count += int(num_word)

    print(uni_count)
