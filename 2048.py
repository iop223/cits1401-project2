## Justin Chong 21508335, Mitchell Wooding [number

from graphics import *
import math
Xmin, Xmax = 0, 720
Ymin, Ymax = 0, 720

#This function is the main control of the flow of the program
#It draws dem boxes
def main():
    win = GraphWin('wewuz', Xmax-Xmin, Ymax-Ymin)    
    win.setCoords(Xmin, Ymin, Xmax, Ymax)
    makeInterface(win)
    x = 0
    

def erase(win):
    rect = Rectangle(Point(Xmin,Xmin), Point(Xmax,Ymax))
    rect.setFill(color_rgb(139,69,19))
    rect.draw(win)

#This function should make the Graphical User Interface i.e. the Entry boxes and the Buttons.
#It should return the variable identifiers of the Buttons and Entry boxes to the calling function. 
def makeInterface(win): #4 marks
    win.setBackground(color_rgb(238,0,238))
    erase(win)
main()
