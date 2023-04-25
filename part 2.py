import tkinter as tk
from tkinter import Frame, Label, CENTER
import random



length= 400
blockcount= 4

upKey= 'w'
downKey= 's'
leftKey= 'a'
rightKey='d'

labelFont=("Arial", 40, 'bold')
gameColor = 'Black'
emptyColor='white'
Colors= {2: 'ghost white' , 4:'light goldenrod', 8:'orange', 16: 'red', 32: 'pink',
               64:'purple', 128: 'blue', 256:'green', 512:'brown',
               1024:'grey', 2048: 'white'}
labelColors='black'
class displaygame(tk.Frame):
    
    def __init__(x):
        tk.Frame.__init__(x)
        x.grid()
        x.master.title('2048')
        x.mainGrid= tk.Frame(x, bg= 'black',
                             bd= 3, width= 600, height=600)
        x.mainGrid.grid(pady=(100, 0))
        
        x.makeFrame()
        x.startGame
        x.mainloop()
        
        

    def makeFrame(x):
        x.block= []
        for a in range(4):
            row=[]
            for b in range(4):
                blockFrame= tk.Frame( x.mainGrid, bg='grey',
                                      width= 150, height= 150)
                
                blockFrame.grid(row= a, column= b,
                        padx=5, pady=5)
                blockNum= tk.Label(x.mainGrid)
                displaygame.configure(x, bg='white')
                blockNum.grid(row= a, column=b)
                blockInfo= {'frame':blockFrame, 'number': blockNum}
                row.append(blockInfo)
            
        x.block.append(row)
        scoreFrame= tk.Frame(x)
        scoreFrame.place(relx= 0.5, y=45, anchor='center')
        tk.Label(scoreFrame, text= 'score: ', font='Arial').grid(row=0)
        x.scoreLabel= tk.Label(scoreFrame, text= '0', font= 'Arial')
        
    def startGame(x):
        x.matrix=[[0]*4 for _ in range(4)]
        row= random.randint(0, 3)
        col= random.randint(0, 3)
        x.matrix[row][col] = 2
        x.block[row][col]['frame'].configure(bg='white')
        x.block[row][col]['number'].configure(bg= 'black', fg='grey',
                                             font= 'Arial', text= '2')
        while(x.matrix[row][col] != 0):
            row= random.randint(0, 3)
            col= random.randint(0, 3)
        x.matrix[row][col] =2
        x.block[row][col]['frame'].configure(bg='white')
        x.block[row][col]['number'].configure(bg= 'black', fg='grey',
                                                font= 'Arial', text= '2')
        x.score= 0
        


displaygame()        


