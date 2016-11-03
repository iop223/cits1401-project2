## Justin Chong 21508335, Mitchell Wooding 22088045

from graphics import *
import math
Xmin, Xmax = 0, 720
Ymin, Ymax = 0, 720

#This function is the main control of the flow of the program
def main():
    win = GraphWin('wewuz', Xmax-Xmin, Ymax-Ymin)    
    win.setCoords(Xmin, Ymin, Xmax, Ymax)
    newGamebutton, quitButton = makeInterface(win)
    x = 0
<<<<<<< HEAD
    while x==0:
        Pt = win.getMouse()
        if isClicked(Pt,quitButton):
            win.close
    
=======

>>>>>>> 3eb3eb2c0e8acc0c2835deb0ff5a50f9eaa43bb4

def erase(win):
    rect = Rectangle(Point(Xmin,Ymin), Point(Xmax,Ymax))
    rect.setFill(color_rgb(139,69,19))
    rect.draw(win)
def drawboxes(win):
    listBox=[]
    for i in range(0,5):
        for j in range(0,5):
            box = Rectangle(Point(Xmin+5+i*100,Ymax-5-j*100), Point(Xmin+100+i*100,Ymax-100-j*100))
            box.setFill(color_rgb(255,0,255))
            box.draw(win)
            listBox.append(box)
            print (listBox[i])
#This function should make the Graphical User Interface i.e. the Entry boxes and the Buttons.
#It should return the variable identifiers of the Buttons and Entry boxes to the calling function. 
def makeInterface(win):
    win.setBackground(color_rgb(139,69,19))
    erase(win)
    drawboxes(win)
<<<<<<< HEAD
    scoreBoard(win)

    #rectangle button with text
    quitButton = Rectangle(Point(Xmax-100, Ymax-50),Point(Xmax, Ymax))
    quitButton.setFill('#568203')
    quitButton.draw(win)
    q = Text(Point(Xmax-50, Ymax-25), "Quit")
    q.draw(win)

    #rectangle button with text
    newGamebutton = Rectangle(Point(Xmax-100, Ymax-110),Point(Xmax, Ymax-60))
    newGamebutton.setFill('#568203')
    newGamebutton.draw(win)
    ng = Text(Point(Xmax-50, Ymax-85), "New Game")
    ng.draw(win)


#This function should take the Point pClick where the mouse was clicked and the button identifier and return True if the click was inside the button otherwise it should return False.
def isClicked(pClick, button):
    if (pClick.getX() > button.getP1().getX()) and (pClick.getY() > button.getP1().getY()) and (pClick.getX() < button.getP2().getX()) and (pClick.getY() < button.getP2().getY()):
        return True


#This function Displays the score
def scoreBoard(win):
    scoreDisplay = Text(Point(Xmin+50,Ymin+50), "fag").draw(win)
=======
    statDisplay(win)

#This function Displays the score
def statDisplay(win):
    #score = calcScore(score)
    #direction = getDirection(direction)
    #success = getSuccess(success)
    scoreDisplay = Text(Point(Xmin+100,Ymin+50), "SCORE").draw(win)
    moveSucces = Text(Point(Xmin+250,Ymin+50), "Move DIRECTION is SUCCESS").draw(win)

>>>>>>> 3eb3eb2c0e8acc0c2835deb0ff5a50f9eaa43bb4

main()
