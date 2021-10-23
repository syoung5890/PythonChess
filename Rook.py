import Piece

class Rook(Piece.Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)

    def __str__(self):
        return "R"

    def move(self,row,col):
        if(row == self.row) or (col == self.col):
            return True
        else:
            return False

    def capture(self,row,col):
        if(row == self.row) or (col == self.col):
            return True
        else:
            return False
