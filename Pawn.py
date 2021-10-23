import Piece


class Pawn(Piece.Piece):
    def __init__(self, row, col, color):
        self.numOfMoves = 0
        super().__init__(row, col, color)
        self.colorfactor = 1
        if color == "WHITE":
            self.colorfactor = -1

    def __str__(self):
        return "P"

    def move(self, row, col,blocked):  # MUST CHECK BOARD TO MAKE SURE SPACE IS AVAILLABLE BEFORE CALLING FUNCTION
        if col == self.col:  # THIS FUNCTION JUST CHECKS IF MOVE IS LEGAL MOVE FOR THE PIECE
            if row - self.row == 2 * self.colorfactor and not blocked:  # IT DOES NOT MAKE THE MOVE OR CHECK IF MOVE IS ILLEGAL BECAUSE OF OTHER PIECES INTERFERING
                if self.numOfMoves == 0:
                    self.numOfMoves += 1
                    return True
                else:
                    return False
            elif row - self.row == 1 * self.colorfactor and not blocked:
                self.numOfMoves += 1
                return True
            else:
                return False
        else:
            return False

    def capture(self, row, col,blocked):
        print("col - self.col ", col - self.col, 1*self.colorfactor)
        print("abs(row - self.row", abs(row-self.row))
        if abs(col - self.col) == 1 and row - self.row == 1*self.colorfactor:
            self.numOfMoves += 1
            print("can capture")
            return True
        else:
            print("can't capture")
            return False

