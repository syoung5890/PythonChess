import Bishop
import King
import Knight
import Pawn
import Queen
import Rook
import copy

class Board:
    def __init__(self):
        self.gameboard = [[0] * 8 for i in range(8)]
        self.blackKing = King.King(0, 4, "BLACK")
        self.whiteKing = King.King(7, 4, "WHITE")
        self.whitePiecesList = []
        self.blackPiecesList = []
        self.capturedByWhite = []
        self.capturedByBlack = []
        self.setPawns(self.whitePiecesList, self.gameboard, 6, "WHITE")
        self.setMajorPieces(self.whitePiecesList, self.gameboard, 7, "WHITE", self.whiteKing)
        self.setPawns(self.blackPiecesList, self.gameboard, 1, "BLACK")
        self.setMajorPieces(self.blackPiecesList, self.gameboard, 0, "BLACK", self.blackKing)
        self.turn = "WHITE"
        self.selectedPiece = 0

    def isPieceInWay(self, piece, row, col):
        if piece.__str__() == "k":
            return False
        if row == piece.row:
            x = 0
        elif row > piece.row:
            x = -1
        else:
            x = 1
        if col == piece.col:
            y = 0
        elif col > piece.col:
            y = -1
        else:
            y = 1
        row += x
        col += y
        if x != 0:
            c = col
            print(piece.row)
            print(piece.col)
            for r in range(row, piece.row, x):
                print("C: ", c)
                print("R: ", r)
                if r > 7 or r < 0 or c > 7 or c < 0:
                    return False
                if self.gameboard[r][c] != 0:
                    return True
                c += y
            return False

        elif y != 0:
            r = row
            for c in range(col, piece.col, y):
                if r > 7 or r < 0 or c > 7 or c < 0:
                    return False
                if self.gameboard[r][c] != 0:
                    return True
                r += x
            return False
        else:
            return False

    def movePiece(self, piece, row, col):
        if piece == 0:
            return False

        if piece.move(row, col,self.isPieceInWay(piece,row,col)) and self.gameboard[row][col] == 0:
            print("Piece moved")
            self.gameboard[row][col] = piece
            self.gameboard[piece.row][piece.col] = 0
            piece.row = row
            piece.col = col
            return True
        else:
            return False

    def capturePiece(self, piece, row, col):
        print("enter capture piece")
        if self.gameboard[row][col] != 0:
            if piece.color == "WHITE" and self.gameboard[row][col].color == "BLACK" and piece.capture(row, col,self.isPieceInWay(piece,row,col)):
                print("seems good")
                self.capturedByWhite.append(self.gameboard[row][col])
                self.blackPiecesList.remove(self.gameboard[row][col])
                self.gameboard[row][col] = 0
                self.gameboard[row][col] = piece
                self.gameboard[piece.row][piece.col] = 0
                piece.row = row
                piece.col = col
                return True
            elif piece.color == "BLACK" and self.gameboard[row][col].color == "WHITE" and piece.capture(row,col,self.isPieceInWay(piece,row,col)):
                self.capturedByBlack.append(self.gameboard[row][col])
                self.whitePiecesList.remove(self.gameboard[row][col])
                self.gameboard[row][col] = 0
                self.gameboard[row][col] = piece
                self.gameboard[piece.row][piece.col] = 0
                piece.row = row
                piece.col = col
                return True
            else:
                return False
        else:
            return False


    def setPawns(self,lst, gameboard, row, color):
        for col in range(8):
            pawn = Pawn.Pawn(row, col, color)
            lst.append(pawn)
            gameboard[row][col] = pawn


    def setMajorPieces(self,lst, gameboard, row, color, kng):
        rook = Rook.Rook(row, 0, color)
        lst.append(rook)
        gameboard[row][0] = rook

        knight = Knight.Knight(row, 1, color)
        lst.append(knight)
        gameboard[row][1] = knight

        bishop = Bishop.Bishop(row, 2, color)
        lst.append(bishop)
        gameboard[row][2] = bishop

        queen = Queen.Queen(row, 3, color)
        lst.append(queen)
        gameboard[row][3] = queen

        # king = King.King(row,4,color)
        lst.append(kng)
        gameboard[row][4] = kng

        bishop = Bishop.Bishop(row, 5, color)
        lst.append(bishop)
        gameboard[row][5] = bishop

        knight = Knight.Knight(row, 6, color)
        lst.append(knight)
        gameboard[row][6] = knight

        rook = Rook.Rook(row, 7, color)
        lst.append(rook)
        gameboard[row][7] = rook

    def selectSquare(self, row, col):
        if self.gameboard[row][col] == 0:
            return False
        elif self.gameboard[row][col].color == self.turn:
            print(self.gameboard[row][col])
            self.selectedPiece = self.gameboard[row][col]
            return True
        else:
            return False

    def targetSquare(self, row, col):
        print("enter target")
        print(self.gameboard[row][col])
        print(self.selectedPiece)
        if self.castle(self.selectedPiece.color,row,col):
            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"
            return True
        temp = copy.deepcopy(self)
        print(temp.turn)
        #         print(temp.selectedPiece)
        if temp.movePiece(temp.selectedPiece, row, col):
            if temp.kingInCheck(temp.turn):
                return False
            else:
                self.movePiece(self.selectedPiece,row,col)
                print("real")
                print(self.gameboard[row][col])
                print(self.turn)
                print("temp")
                print(temp.gameboard[row][col])
                if self.turn == "WHITE":
                    self.turn = "BLACK"
                else:
                    self.turn = "WHITE"
                print(self.turn)
                return True
        elif temp.capturePiece(temp.selectedPiece, row, col):
            print("heya")
            if temp.kingInCheck(temp.turn):
                return False
            else:
                self.capturePiece(self.selectedPiece,row,col)
                if self.turn == "WHITE":
                    self.turn = "BLACK"
                else:
                    self.turn = "WHITE"
                return True
        else:
            return False

    def kingInCheck(self, color):
        temp = copy.deepcopy(self)
        if color == "WHITE":
            # LOOP THROUGH BLACK PIECES AND CHECK IF ANY PIECES CAN ATTACK WHITE KING
            for x in temp.blackPiecesList:
                if temp.capturePiece(x, temp.whiteKing.row, temp.whiteKing.col):
                    print(x)
                    print("king in check")
                    return True
            print("king not in check")
            return False
        else:
            # LOOP THROUGH WHITE PIECES AND CHECK IF ANY PIECES CAN ATTACK BLACK KING
            for x in temp.whitePiecesList:
                if temp.capturePiece(x, temp.blackKing.row, temp.blackKing.col):
                    print("king in check")
                    return True
            print("king not in check")
            return False

    def kingInCheckMate(self,color):
        pass

    def castle(self,color,row,col):
        print("ENTER CASTLE")
        print(self.selectedPiece)
        if self.kingInCheck(color):
            print("KING IN CHECK CAN't CASTLE")
            return False
        elif self.selectedPiece.__str__() == "K":
            print("PIECE IS KING")
            if self.selectedPiece.color == "WHITE":
                print("PIECE IS WHITE")
                print("ROW ", row)
                print("COL ", col)
                if row == 7:
                    if col == 2:
                        if self.gameboard[7][0].__str__() == "R" and not self.isPieceInWay(self.selectedPiece,7,0):
                            if self.selectedPiece.numOfMoves == 0 and self.gameboard[7][0].numOfMoves == 0:
                                print("CAN CASTLE")
                                temp = copy.deepcopy(self)
                                temp.gameboard[7][2] = self.selectedPiece
                                temp.gameboard[7][4] = 0
                                temp.selectedPiece.row = 7
                                temp.selectedPiece.col = 2
                                temp.selectedPiece.numOfMoves += 1
                                temp.gameboard[7][3] = self.gameboard[7][0]
                                temp.gameboard[7][0] = 0
                                temp.gameboard[7][3].col = 3
                                temp.gameboard[7][3].numOfMoves +=1
                                if temp.kingInCheck(temp.turn):
                                    return False
                                else:
                                    self.gameboard[7][2] = self.selectedPiece
                                    self.gameboard[7][4] = 0
                                    self.selectedPiece.row = 7
                                    self.selectedPiece.col = 2
                                    self.selectedPiece.numOfMoves += 1
                                    self.gameboard[7][3] = self.gameboard[7][0]
                                    self.gameboard[7][0] = 0
                                    self.gameboard[7][3].col = 3
                                    self.gameboard[7][3].numOfMoves += 1
                                    return True
                            else:
                                return False
                        else:
                            return False

                    elif col == 6:
                        if self.gameboard[7][7].__str__() == "R" and not self.isPieceInWay(self.selectedPiece,7,7):
                            if self.selectedPiece.numOfMoves == 0 and self.gameboard[7][7].numOfMoves == 0:
                                temp = copy.deepcopy(self)
                                temp.gameboard[7][6] = self.selectedPiece
                                temp.gameboard[7][4] = 0
                                temp.selectedPiece.row = 7
                                temp.selectedPiece.col = 6
                                temp.selectedPiece.numOfMoves += 1
                                temp.gameboard[7][5] = self.gameboard[7][0]
                                temp.gameboard[7][7] = 0
                                temp.gameboard[7][5].col = 3
                                temp.gameboard[7][5].numOfMoves += 1
                                if temp.kingInCheck(self.turn):
                                    return False
                                else:
                                    self.gameboard[7][6] = self.selectedPiece
                                    self.gameboard[7][4] = 0
                                    self.selectedPiece.row = 7
                                    self.selectedPiece.col = 6
                                    self.selectedPiece.numOfMoves += 1
                                    self.gameboard[7][5] = self.gameboard[7][0]
                                    self.gameboard[7][7] = 0
                                    self.gameboard[7][5].col = 3
                                    self.gameboard[7][5].numOfMoves += 1
                                    return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                if row == 0:
                    if col == 2:
                        if self.gameboard[0][0].__str__() == "R" and not self.isPieceInWay(self.selectedPiece,0,0):
                            if self.selectedPiece.numOfMoves == 0 and self.gameboard[0][0].numOfMoves == 0:
                                print("CAN CASTLE")
                                temp = copy.deepcopy(self)
                                temp.gameboard[0][2] = self.selectedPiece
                                temp.gameboard[0][4] = 0
                                temp.selectedPiece.row = 0
                                temp.selectedPiece.col = 2
                                temp.selectedPiece.numOfMoves += 1
                                temp.gameboard[0][3] = self.gameboard[7][0]
                                temp.gameboard[0][0] = 0
                                temp.gameboard[0][3].col = 3
                                temp.gameboard[0][3].numOfMoves +=1
                                if temp.kingInCheck(temp.turn):
                                    return False
                                else:
                                    self.gameboard[0][2] = self.selectedPiece
                                    self.gameboard[0][4] = 0
                                    self.selectedPiece.row = 0
                                    self.selectedPiece.col = 2
                                    self.selectedPiece.numOfMoves += 1
                                    self.gameboard[0][3] = self.gameboard[7][0]
                                    self.gameboard[0][0] = 0
                                    self.gameboard[0][3].col = 3
                                    self.gameboard[0][3].numOfMoves += 1
                                    return True
                            else:
                                return False
                        else:
                            return False

                    elif col == 6:
                        if self.gameboard[0][7].__str__() == "R" and not self.isPieceInWay(self.selectedPiece,0,7):
                            if self.selectedPiece.numOfMoves == 0 and self.gameboard[0][7].numOfMoves == 0:
                                temp = copy.deepcopy(self)
                                temp.gameboard[0][6] = self.selectedPiece
                                temp.gameboard[0][4] = 0
                                temp.selectedPiece.row = 0
                                temp.selectedPiece.col = 6
                                temp.selectedPiece.numOfMoves += 1
                                temp.gameboard[0][5] = self.gameboard[0][0]
                                temp.gameboard[0][7] = 0
                                temp.gameboard[0][5].col = 3
                                temp.gameboard[0][5].numOfMoves += 1
                                if temp.kingInCheck(self.turn):
                                    return False
                                else:
                                    self.gameboard[0][6] = self.selectedPiece
                                    self.gameboard[0][4] = 0
                                    self.selectedPiece.row = 0
                                    self.selectedPiece.col = 6
                                    self.selectedPiece.numOfMoves += 1
                                    self.gameboard[0][5] = self.gameboard[0][0]
                                    self.gameboard[0][7] = 0
                                    self.gameboard[0][5].col = 3
                                    self.gameboard[0][5].numOfMoves += 1
                                    return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False

