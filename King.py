import Piece

class King(Piece.Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.numOfMoves = 0

    def __str__(self):
        return "K"

    def move(self, row, col,blocked):
        if (abs(row - self.row) <= 1) and (abs(col - self.col) <= 1):
            self.numOfMoves += 1
            return True
        else:
            return False

    def capture(self, row, col,blocked):
        if self.move(row,col,blocked):
            return True
        else:
            return False