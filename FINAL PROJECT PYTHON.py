#2048
#Lana Lerner and Amanda McEachern Section 7
#press the up, down, left, and right keys to play
# don't hold down a key or it will take a long time when it checks
#if there are any horizontal or vertical moves

import tkinter as tk
from tkinter import Frame, Label, CENTER
import random

blockColors = {2: 'misty rose' , 4:'deep pink', 8:'medium violet red', 16: 'red', 32: 'hot pink',
               64:'purple', 128: 'blue', 256:'green', 512:'brown',
               1024:'grey', 2048: 'white'}

emptyBlockColor = "grey"
labelColors='black'
gameColor = {2: 'misty rose' , 4:'deep pink', 8:'medium violet red', 16: 'red', 32: 'hot pink',
               64:'purple', 128: 'blue', 256:'green', 512:'brown',
               1024:'grey', 2048: 'white'}

font = ("Arial", 40, "bold")
scoreFont = ("Arial", 20, "bold")

class displayGame(tk.Frame):
    def __init__(x):
        tk.Frame.__init__(x)
        x.grid()
        x.master.title('2048')
        x.mainGrid= tk.Frame(x, bg="black",
                             bd= 3, width= 600, height=600)
        x.mainGrid.grid(pady=(100, 0))

        x.GUI()
        x.startGame()

        #these are needed to use the up, down, left, and right keys to play the game
        x.master.bind("<Left>", x.left)
        x.master.bind("<Right>", x.right)
        x.master.bind("<Up>", x.up)
        x.master.bind("<Down>", x.down)

        x.mainloop()

    def GUI(x):
        x.block = []
        for a in range(4):
            row = []
            for b in range(4):
                blockFrame = tk.Frame(x.mainGrid, bg="grey",
                                      width= 150, height= 150)
                blockFrame.grid(row= a, column= b, padx=5, pady=5)
                blockNum= tk.Label(x.mainGrid, bg="grey")
                blockNum.grid(row= a, column=b)
                blockInfo= {'frame':blockFrame, 'number': blockNum}
                row.append(blockInfo)
            x.block.append(row)

            scoresFrame= tk.Frame(x)
            scoresFrame.place(relx= 0.5, y=45, anchor='center')
            tk.Label(scoresFrame, text= 'score: ', font=scoreFont).grid(row=0)
            x.scoreLabel= tk.Label(scoresFrame, text= '0', font= scoreFont)
            x.scoreLabel.grid(row=1)

    def startGame(x): #this creates the initial 2 blocks at random
        x.matrix = [[0] * 4 for _ in range(4)]
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        x.matrix[row][col] = 2
        x.block[row][col]['frame'].configure(bg=blockColors[2])
        x.block[row][col]['number'].configure(bg= blockColors[2], fg=labelColors,
                                             font= font, text= '2')

        while (x.matrix[row][col] != 0):
            row= random.randint(0, 3)
            col= random.randint(0, 3)
        x.matrix[row][col] =2
        x.block[row][col]['frame'].configure(bg=blockColors[2])
        x.block[row][col]['number'].configure(bg= blockColors[2], fg=labelColors,
                                             font= font, text= '2')
        x.score = 0


    def compressLeft(x): 
        newMatrix = [[0] * 4 for _ in range(4)]
        for a in range(4):
            position = 0
            for b in range(4):
                if x.matrix[a][b] !=0:
                    newMatrix[a][position] = x.matrix[a][b]
                    position +=1
        x.matrix = newMatrix

    def combineHorizontal(x):
        for a in range(4):
            for b in range(3):
                if x.matrix[a][b] != 0 and x.matrix[a][b] == x.matrix[a][b+1]:
                    x.matrix[a][b] *= 2
                    x.matrix[a][b+1] = 0
                    x.score += x.matrix[a][b]
    def reverse(x):
        newMatrix = []
        for a in range(4):
            newMatrix.append([])
            for b in range(4):
                newMatrix[a].append(x.matrix[a][3 - b])
        x.matrix = newMatrix

    def flipMatrixDiagonally(x):
        newMatrix = [[0] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                newMatrix[a][b] = x.matrix[b][a]
        x.matrix = newMatrix

    def newTile(x): #adds a 2 or 4 tile randomly 
        row = random.randint(0,3)
        col = random.randint(0,3)
        while (x.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        x.matrix[row][col] = random.choice([2,4])

    def newGUI(x):
        for a in range(4):
            for b in range(4):
                cellValue = x.matrix[a][b]
                if cellValue == 0:
                    x.block[a][b]["frame"].configure(bg=emptyBlockColor)
                    x.block[a][b]["number"].configure(bg=emptyBlockColor, text="")
                else:
                    x.block[a][b]["frame"].configure(bg=gameColor[cellValue])
                    x.block[a][b]["number"].configure(bg=blockColors[cellValue],
                                                      fg=labelColors,
                                                      font=font,
                                                      text=str(cellValue))

        x.scoreLabel.configure(text=x.score)
        x.update_idletasks()        

    def up(x, event):
        x.flipMatrixDiagonally()
        x.compressLeft()
        x.combineHorizontal()
        x.compressLeft()
        x.flipMatrixDiagonally()
        x.newTile()
        x.newGUI()
        x.endGame()

    def down(x, event):
        x.flipMatrixDiagonally()
        x.reverse()
        x.compressLeft()
        x.combineHorizontal()
        x.compressLeft()
        x.reverse()
        x.flipMatrixDiagonally()
        x.newTile()
        x.newGUI()
        x.endGame()

    def right(x, event):
        x.reverse()
        x.compressLeft()
        x.combineHorizontal()
        x.compressLeft()
        x.reverse()
        x.newTile()
        x.newGUI()
        x.endGame()

    def left(x, event):
        x.compressLeft()
        x.combineHorizontal()
        x.compressLeft()
        x.newTile()
        x.newGUI()
        x.endGame()

    def horizontal(x): #checks for horizontal moves
        for a in range(4):
            for b in range(3):
                if x.matrix[a][b] == x.matrix[a][b+1]:
                    return True
        return False

    def vertical(x): #checks for vertical moves
        for a in range(3):
            for b in range(4):
                if x.matrix[a][b] == x.matrix[a+1][b]:
                    return True
        return False

    def endGame(x): #determines if you win or lose the game
        if any(2048 in row for row in x.matrix):
              frame = tk.Frame(x.grid, borderwidth = 2)
              frame.place(relx = 0.5, rely = 0.5, anchor ="center")
              tk.Label(frame,font = font, text = "You win!").pack()
        elif not any(0 in row for row in x.matrix) and not x.horizontal() and not x.vertical():
            frame = tk.Frame(x.mainGrid, borderwidth = 2)
            frame.place(relx = 0.5, rely = 0.5, anchor ="center")
            tk.Label(frame,font = font, text = "Game over!").pack()

def main():
    displayGame()
  


if __name__ == "__main__":
    main()
                


    
    
