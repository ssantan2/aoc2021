from collections import defaultdict


class Board:


    def __init__(self, board_struct):
        self._setup(board_struct)

    def _setup(self, board_struct):
        self.rows = [0 for _ in board_struct]
        self.cols = [0 for _ in board_struct]
        self.number_placement = defaultdict(list)

        for i, row in enumerate(board_struct):
            for j, number in enumerate(row):
                self.number_placement[number].append((i,j))
                self.rows[i] += number
                self.cols[j] += number

    def mark_number(self, num):
        locations = self.number_placement.get(num, [])

        for x, y in locations:
            self.rows[x] -= num
            self.cols[y] -= num
            if self.rows[x] == 0:
                return True
            if self.cols[y] == 0:
                return True

        return False

    def final_score(self, num):
        numm = 0
        for row in self.rows:
            numm += row

        return numm * num


with open("input1.txt") as f:
    lines = f.readlines()

    numbers_to_call = [int(num) for num in lines[0].replace("\n", "").split(",")]
    boards = lines[2:]

    board_structs = []

    new_board = []
    for board_line in boards:
        int_line = [int(num) for num in board_line.replace("\n", "").split()]
        if len(int_line) == 0:
            board_structs.append(Board(new_board))
            new_board = []
        else:
            new_board.append(int_line)

    if len(new_board) != 0:
        board_structs.append(Board(new_board))

    final_score = 0
    for num in numbers_to_call:
        if final_score > 0:
            break
        for board in board_structs:
            win = board.mark_number(num)
            if win:
                final_score = board.final_score(num)

    print(final_score)
