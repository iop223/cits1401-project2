## Justin Chong 21508335, Mitchell Wooding 22088045

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
def drawboxes(win):
    for i in range(0,5):
        for j in range(0,5):
            box = Rectangle(Point(Xmin+20+i*5,Xmax+20+j*5), Point(Xmin+50+j*5,Ymax+50+j*5))
            box.setFill(color_rgb(255,0,255))
            box.draw(win)

#This function should make the Graphical User Interface i.e. the Entry boxes and the Buttons.
#It should return the variable identifiers of the Buttons and Entry boxes to the calling function. 
def makeInterface(win):
    win.setBackground(color_rgb(139,69,19))
    erase(win)
    drawboxes(win)
main()
