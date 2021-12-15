from collections import defaultdict


def radiate(basin_value, board, x, y, seen_board):
    val = board[x][y]
    if val != 9:
        basin_value += 1
        seen_board[x][y] = True
    if val == 9:
        return basin_value

    if x < len(board) - 1 and not seen_board[x + 1][y]:
        basin_value = radiate(basin_value, board, x + 1, y, seen_board)
    if x > 0 and not seen_board[x-1][y]:
        basin_value = radiate(basin_value, board, x - 1, y, seen_board)
    if y < len(board[x]) - 1 and not seen_board[x][y + 1]:
        basin_value = radiate(basin_value, board, x, y + 1, seen_board)
    if y > 0 and not seen_board[x][y - 1]:
        basin_value = radiate(basin_value, board, x, y - 1, seen_board)

    return basin_value


with open("input.txt") as f:
    lines = f.readlines()
    board = [
        [int(l) for l in line if l != "\n"]
        for line in lines
    ]

    seen_board = []
    for line in lines:
        low_row = []
        for char in line:
            low_row.append(False)
        seen_board.append(low_row)

    basins = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if not seen_board[x][y]:
                cur_basin_value = radiate(0, board, x, y, seen_board)
                if cur_basin_value > 0:
                    basins.append(cur_basin_value)

    mul_basins = sorted(basins)[-3:]
    num_e = 1
    for num in mul_basins:
        num_e *= num

    print(num_e)
