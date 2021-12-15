
def increment(board):
    for y, row in enumerate(board):
        for x, _ in enumerate(row):
            board[x][y] += 1


def flash(board, x, y):
    if board[x][y] <= 9:
        return 0

    board[x][y] = 0
    flash_count = 1
    x1 = False
    x2 = False
    y1 = False
    y2 = False

    if x < len(board) - 1:
        x1 = True
        if board[x + 1][y] > 0:
            board[x + 1][y] += 1
            flash_count += flash(board, x + 1, y)
    if x > 0:
        x2 = True
        if board[x - 1][y] > 0:
            board[x - 1][y] += 1
            flash_count += flash(board, x - 1, y)

    if y < len(board[x]) - 1 > 0:
        y1 = True
        if board[x][y + 1]:
            board[x][y + 1] += 1
            flash_count += flash(board, x, y + 1)

    if y > 0:
        y2 = True
        if board[x][y - 1] > 0:
            board[x][y - 1] += 1
            flash_count += flash(board, x, y - 1)

    if x1 and y1:
         if board[x + 1][y + 1] > 0:
            board[x + 1][y + 1] += 1
            flash_count += flash(board, x + 1, y + 1)

    if x1 and y2:
         if board[x + 1][y - 1] > 0:
            board[x + 1][y - 1] += 1
            flash_count += flash(board, x + 1, y - 1)

    if x2 and y1:
         if board[x - 1][y + 1] > 0:
            board[x - 1][y + 1] += 1
            flash_count += flash(board, x - 1, y + 1)

    if x2 and y2:
         if board[x - 1][y - 1] > 0:
            board[x - 1][y - 1] += 1
            flash_count += flash(board, x - 1, y - 1)

    return flash_count

def check_board(board):
    flash_count = 0
    for y, row in enumerate(board):
        for x, _ in enumerate(row):
            flash_count += flash(board, x, y)
    return flash_count

with open("input.txt") as f:
    lines = f.readlines()

    board = [
        [int(l) for l in line if l != "\n"]
        for line in lines
    ]

    flash_count = 0
    steps_taken = 0
    for step in range(0, 10000):
        steps_taken += 1
        increment(board)
        cur_flash_count = check_board(board)
        if cur_flash_count == 100:
            print(steps_taken)
            break
        flash_count += cur_flash_count

    print(flash_count)

