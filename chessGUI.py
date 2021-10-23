import tkinter as tk
import Board
import os

from tkinter import *

from PIL import Image, ImageTk


def makeFunc(i, j):
    return lambda: clickOnSquare(i, j)


def deleteButtons():
    for x in buttonList:
        x.destroy()


def clickOnSquare(row, col):
    global selected
    if selected:
        if newgame.gameboard[row][col] != 0:
            if newgame.gameboard[row][col].color == newgame.turn:
                newgame.selectSquare(row, col)
                print("selected")
            elif newgame.targetSquare(row, col):
                deleteButtons()
                drawBoard(newgame, window, newgame.gameboard, buttonList)
                print(newgame.turn)
                selected = False
        elif newgame.targetSquare(row, col):
            deleteButtons()
            drawBoard(newgame, window, newgame.gameboard, buttonList)
            print(newgame.turn)
            selected = False
        else:
            pass
    else:
        if newgame.selectSquare(row, col):
            print("selected")
            selected = True


def drawBoard(game, frame, board, buttonList):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                if (i + j) % 2 == 0:
                    load = Image.open("DarkSquare.png")
                    render = ImageTk.PhotoImage(load)
                    img = Label(frame, image=render)
                    img.image = render
                    sqr = Button(frame, image=render, command=makeFunc(i, j))
                    sqr.place(x=200 + j * 75, y=200 + i * 75)
                    buttonList.append(sqr)
                else:
                    load = Image.open("LightSquare.png")
                    render = ImageTk.PhotoImage(load)
                    img = Label(frame, image=render)
                    img.image = render
                    sqr = Button(frame, image=render, command=makeFunc(i, j))
                    sqr.place(x=200 + j * 75, y=200 + i * 75)
                    buttonList.append(sqr)
            elif board[i][j].__str__() == "P":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhitePawnDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhitePawnLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackPawnDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackPawnLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

            elif board[i][j].__str__() == "R":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhiteRookDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhiteRookLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackRookDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackRookLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

            elif board[i][j].__str__() == "k":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhiteKnightDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhiteKnightLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackKnightDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackKnightLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

            elif board[i][j].__str__() == "B":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhiteBishopDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhiteBishopLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackBishopDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackBishopLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

            elif board[i][j].__str__() == "Q":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhiteQueenDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhiteQueenLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackQueenDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackQueenLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

            elif board[i][j].__str__() == "K":
                if board[i][j].color == "WHITE":
                    if (i + j) % 2 == 0:
                        load = Image.open("WhiteKingDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("WhiteKingLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                else:
                    if (i + j) % 2 == 0:
                        load = Image.open("BlackKingDarkSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)
                    else:
                        load = Image.open("BlackKingLightSquare.png")
                        render = ImageTk.PhotoImage(load)
                        img = Label(frame, image=render)
                        img.image = render
                        sqr = Button(frame, image=render, command=makeFunc(i, j))
                        sqr.place(x=200 + j * 75, y=200 + i * 75)
                        buttonList.append(sqr)

os.chdir("assets")
selected = False
newgame = Board.Board()
window = tk.Tk()
window.title("CHESS")
window.geometry("1000x1000")
buttonList = []
drawBoard(newgame, window, newgame.gameboard, buttonList)
window.mainloop()

