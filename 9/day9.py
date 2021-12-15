from collections import defaultdict


with open("input.txt") as f:
    lines = f.readlines()
    lines = [
        [int(l) for l in line if l != "\n"]
        for line in lines
    ]

    low_points = []
    for line in lines:
        low_row = []
        for char in line:
            low_row.append(0)
        low_points.append(low_row)


    current_basin = 1
    basin_dict = default_dict(int)
    for i, line in enumerate(lines):
        for y, char in enumerate(line):
            char = int(char)
            right_char = None
            down_char = None
            if y < len(line) -1:
                right_char = int(lines[i][y+1])
            if i < len(lines) - 1:
                down_char = int(lines[i+1][y])

            if char != 9 and low_points[i][y] == 0:
                low_points[i][y] = current_basin
                basin_dict[current_basin] += char
            if right_char != 9 and low_points[i][y+1] == 0:
                low_points[i][y+1] = current_basin
                basin_dict[current_basin] += char
            if left_char != 9 and low_points[i+1][y] == 0:
                low_points[i+1][y] = current_basin
                basin_dict[current_basin] += char


            # look forward
            if y < len(line) - 1:
                if char < int(lines[i][y+1]):
                    low_points[i][y+1] = False
                else:
                                # Look above
            if i < len(lines) - 1:
                if char < int(lines[i + 1][y]):
                    low_points[i + 1][y] = False
                else:
                    low_points[i][y] = current_basin
                    basin_dict[current_basin] += char

            if low_points[i][y]:
                low_num += char + 1
    print(low_num)
