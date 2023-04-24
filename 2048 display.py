import tkinter with Frame, Label, CENTER


length= 400
cell.count= 4

up.key= 'w'
down.key= 's'
left.key= 'a'
right.key='d'

label_font("Arial" 40, 'bold')
game_color = 'black'

title_colors= {2: 'white', 4:'yellow', 8:'orange', 16: 'red', 32: 'pink',
               64:'purple', 128: 'blue', 256:'green', 512:'brown',
               1024:'grey', 2048: 'white'}
label_colors('black')

def frame(x):
    Frame.frame(x)
    x.grid
    x.title('2048')
    x.bind("<Key>"), x.key_press
    commands= {up.key: game_functions.move_up,
               down.key: game_functions.move_down,
               left.key: game_functions.move_left,
               right.key= game_functions.move_right}
    x.grid_cells = []
    x.build.grid
    x.draw_grid_cells()


def build.grid(x):
    backround= Frame(x, bg = game_color, width = length/cell.count,
                     height = length/cell.count)
    backround.grid()
    for col in range(cell.count):
        cell= Frame(backround, bg, width, height)
    
        
