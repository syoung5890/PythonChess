import Piece

class Rook(Piece.Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        self.numOfMoves = 0

    def __str__(self):
        return "R"

    def move(self,row,col,blocked):
        if((row == self.row) or (col == self.col)) and not blocked:
            self.numOfMoves += 1
            return True
        else:
            return False

    def capture(self,row,col, blocked):
        if self.move(row,col,blocked):
            return True
        else:
            return False
