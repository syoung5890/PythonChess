import Piece

class Knight(Piece.Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def __str__(self):
        return "k"

    def move(self, row, col,blocked):
        if (abs(row - self.row) == 2) and (abs(col - self.col) == 1):
            return True
        elif (abs(row - self.row) == 1) and (abs(col - self.col) == 2):
            return True
        else:
            return False

    def capture(self, row, col,blocked):
        if (abs(row - self.row) == 2) and (abs(col - self.col) == 1):
            return True
        elif (abs(row - self.row) == 1) and (abs(col - self.col) == 2):
            return True
        else:
            return False
