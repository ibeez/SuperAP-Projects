from random import randrange
import PySimpleGUI as sg 
from player import player 
#set up a blank maze with a viable space in the middle 
rows, cols = (11,11)
arr = [[False for i in range(cols)]for j in range(rows)]  
arr[5][5] = True

#attempt 2 - intends to create "arms" of the maze by increasing the number of squares altered on each iteration to 2 
#for loop sets the code up to create three valid paths 
def craftmaze():
    for i in range(0,3):
        #generates a random square to be made navigable 
        #each statement also makes the square one further in that direction navigable, if it is not outside the bounds of the array 
        midX, midY = (5,5) 
        while True:
            coin1 = randrange(4)
            if(coin1 == 0):
                midX += 1
                arr[midX][midY] = True
                if(midX < cols - 1):
                    midX += 1
                    arr[midX][midY] = True
            if(coin1 == 1):
                midX -= 1
                arr[midX][midY] = True
                if(midX > 0):
                    midX -= 1
                    arr[midX][midY] = True
            if(coin1 == 2):
                midY += 1
                arr[midX][midY] = True
                if(midY < cols - 1):
                    midY += 1
                    arr[midX][midY] = True
            if(coin1 == 3):
                midY -= 1
                arr[midX][midY] = True
                if(midY > 0):
                    midY -= 1
                    arr[midX][midY] = True 
            if(midX == 0 or midX == cols - 1 or midY == 0 or midY == cols - 1):
                break 
#an old function intended mostly for testing. it prints squares that can be moved in as empty and squares that cannot be navigated as filled
def printmaze():
    #translate array to emojis and print 
    arremoji = [["" for i in range(cols)]for j in range(rows)]  
    for i in range(0,len(arremoji)):
        for j in range(0,len(arremoji[0])):
            if arr[i][j]:
                arremoji[i][j] = '□'
            else:
                arremoji[i][j] = '■'
    arremoji[5][5] = "☻"
    for i in range(0,len(arremoji)):
        print(arremoji[i])

craftmaze()
printmaze()
adventurer = player(5,5)
#create a "player" for gameplay
#create an empty layout for grapgics 
layout = [[sg.Output(size=(50,10))],[sg.Button('forward')],[sg.Button('left'),sg.Button('right')],[sg.Button('back')]]
#display as window 
window = sg.Window("maze",layout,element_justification='c')
print("you find yourself in a mysterious maze surrounded by buttons. What do you press?")
while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'forward':
        if arr[adventurer.ypos - 1][adventurer.xpos]:
            print("you take a step forward")
            adventurer.move('up')
        else:
            print("this way is blocked! try a different direction")
    if event == 'left':
        if arr[adventurer.ypos][adventurer.xpos - 1]:
            print("you take a step left")
            adventurer.move('left') 
        else:
            print("this way is blocked! try a different direction")
    if event == 'right': 
        if arr[adventurer.ypos][adventurer.xpos + 1]:
            print("you take a step right")
            adventurer.move('right') 
        else:
            print("this way is blocked! try a different direction")
    if event == 'back':
        if arr[adventurer.ypos + 1][adventurer.xpos]:
            print("you take a step backwards")
            adventurer.move('down') 
        else:
            print("this way is blocked! try a different direction")
    if(adventurer.xpos == 0 or adventurer.xpos == rows - 1 or adventurer.ypos == 0 or adventurer.ypos == rows - 1):
        
        break

window.close()