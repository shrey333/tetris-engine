from array import array
from collections import deque
import sys

WIDTH = 10
HEIGHT = 100
EMPTY, BLOCK = 0, 1

SHAPES = {
    "Q": ((1, 1), (1, 1)),
    "Z": ((1, 1, 0), (0, 1, 1)),
    "S": ((0, 1, 1), (1, 1, 0)),
    "T": ((1, 1, 1), (0, 1, 0)),
    "I": ((1, 1, 1, 1),),
    "L": ((1, 0), (1, 0), (1, 1)),
    "J": ((0, 1), (0, 1), (1, 1)),
}


class TetrisGame:
    def __init__(self):
        self.board = deque([array("B", [EMPTY] * WIDTH) for _ in range(HEIGHT)])
        self.empty_row = array("B", [EMPTY] * WIDTH)

    def clear_rows(self):
        row = len(self.board) - 1
        while row >= 0:
            if all(cell == BLOCK for cell in self.board[row]):
                self.board.remove(self.board[row])
                self.board.appendleft(array("B", self.empty_row))
            row -= 1

    def get_height(self):
        for i, row in enumerate(self.board):
            if any(cell == BLOCK for cell in row):
                return len(self.board) - i
        return 0

    def check_collision(self, shape, row, col):
        for i, shape_row in enumerate(shape):
            for j, cell in enumerate(shape_row):
                if cell and self.board[row + i][col + j]:
                    return True
        return False

    def find_drop_height(self, shape, col):
        shape_height = len(shape)
        for row in range(len(self.board) - shape_height + 1):
            if self.check_collision(shape, row, col):
                return row - 1
        return len(self.board) - shape_height

    def place_shape(self, shape, row, col):
        for i, shape_row in enumerate(shape):
            for j, cell in enumerate(shape_row):
                if cell:
                    self.board[row + i][col + j] = BLOCK

    def play_move(self, shape_type, col):
        if shape_type not in SHAPES:
            return

        shape = SHAPES[shape_type]
        row = self.find_drop_height(shape, col)

        if row >= 0:
            self.place_shape(shape, row, col)
            self.clear_rows()

    def play_sequence(self, sequence):
        for move in sequence.strip().split(","):
            if len(move) >= 2:
                self.play_move(move[0], int(move[1]))
        return self.get_height()


def main():
    try:
        for line in sys.stdin:
            if line.strip():
                height = TetrisGame().play_sequence(line)
                print(height)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
