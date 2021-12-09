import PySimpleGUI as sg 
class player: 
    #initializes player with a given postion in the maze, and the "map" that the maze creates
    def __init__(self,x,y):
        self.xpos = x
        self.ypos = y
        #place player in the map 
    def move(self, keyword):
        #depending on input, changes location of player 
        if(keyword == 'up'):
            self.ypos -= 1
            #^
        if(keyword == 'down'):
            self.ypos += 1
            #down
        if(keyword == 'left'):
            self.xpos -= 1 
            #<---
        if(keyword == 'right'):
            self.xpos += 1 
            #--->
        
