## Justin Chong 21508335, Mitchell Wooding 22088045

from graphics import *
import math
import box
import random
from box import *
Xmin, Xmax = 0, 720
Ymin, Ymax = 0, 720

#This function is the main control of the flow of the program
def main():
    win = GraphWin('wewuz', Xmax-Xmin, Ymax-Ymin)    
    win.setCoords(Xmin, Ymin, Xmax, Ymax)
    quitButton, newGamebutton, upButton, downButton, leftButton, rightButton, upBorder, downBorder, leftBorder, rightBorder = makeInterface(win)
    x = 0
    gameState = newGamestate()
    print(gameState)
    print("shift up")
    print(clockwise(gameState))
    while x==0:
        Pt = win.getMouse()
        if isClicked(Pt,quitButton):
            win.close()
        elif isClicked(Pt,newGamebutton):
            print ("Create new game")
        elif isClicked(Pt,upButton) or isClicked(Pt,upBorder):
            print ("up")
        elif isClicked(Pt,downButton) or isClicked(Pt,downBorder):
            print ("down")
        elif isClicked(Pt,leftButton) or isClicked(Pt,leftBorder):
            print ("left")
        elif isClicked(Pt,rightButton) or isClicked(Pt,rightBorder):
            print ("right")

            
def erase(win):
    rect = Rectangle(Point(Xmin,Ymin), Point(Xmax,Ymax))
    rect.setFill(color_rgb(139,69,19))
    rect.draw(win)
    
def drawboxes(win):
    box = Box()
    listBox=[]
    x=0
    for i in range(0,5):
        for j in range(0,5):
            square = Rectangle(Point(Xmin+5+i*100,Ymax-5-j*100), Point(Xmin+100+i*100,Ymax-100-j*100))
            square = isHighlited(box,square)
            listBox.append(box)
            square.draw(win)
            x=x+1
            
def isHighlited(box,square):
    square.setFill(color_rgb(255,0,255))
    x = Box.getHighlight()
    print (x)
    if x==0:
        square.setFill(color_rgb(0,255,0))
    return square
#This function should make the Graphical User Interface i.e. the Entry boxes and the Buttons.
#It should return the variable identifiers of the Buttons and Entry boxes to the calling function. 
def makeInterface(win):
    win.setBackground(color_rgb(139,69,19))
    erase(win)
    drawboxes(win)
    statDisplay(win)

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

    #rectangle button with text
    upButton = Rectangle(Point(Xmin+575, Ymin+ 80),Point(Xmin+625,Ymin+120))
    upButton.setFill('#568203')
    upButton.draw(win)
    ng = Text(Point(Xmin+600,Ymin+100), "up")
    ng.draw(win)

    #rectangle button with text
    downButton = Rectangle(Point(Xmin+575, Ymin+30),Point(Xmin+625,Ymin+70))
    downButton.setFill('#568203')
    downButton.draw(win)
    ng = Text(Point(Xmin+600,Ymin+50), "down")
    ng.draw(win)

    #rectangle button with text
    leftButton = Rectangle(Point(Xmin+525, Ymin+30),Point(Xmin+575,Ymin+70))
    leftButton.setFill('#568203')
    leftButton.draw(win)
    ng = Text(Point(Xmin+550,Ymin+50), "left")
    ng.draw(win)

    #rectangle button with text
    rightButton = Rectangle(Point(Xmin+625, Ymin+30),Point(Xmin+675,Ymin+70))
    rightButton.setFill('#568203')
    rightButton.draw(win)
    ng = Text(Point(Xmin+650,Ymin+50), "right")
    ng.draw(win)

    #clicking on the top row of squares moves up
    upBorder = Rectangle(Point(Xmin+105, Ymin+620),Point(Xmin+400,Ymin+715))

    #clicking on the bottom row of squares moves down
    downBorder = Rectangle(Point(Xmin+105, Ymin+220),Point(Xmin+400,Ymin+315))

    #clicking on the left row of squares moves left
    leftBorder = Rectangle(Point(Xmin+5, Ymin+320),Point(Xmin+100,Ymin+615))

    #clicking on the right row of squares moves right
    rightBorder = Rectangle(Point(Xmin+405, Ymin+320),Point(Xmin+500,Ymin+615))

    return quitButton, newGamebutton, upButton, downButton, leftButton, rightButton, upBorder, downBorder, leftBorder, rightBorder


#This function should take the Point pClick where the mouse was clicked and the button identifier and return True if the click was inside the button otherwise it should return False.
def isClicked(pClick, button):
    if (pClick.getX() > button.getP1().getX()) and (pClick.getY() > button.getP1().getY()) and (pClick.getX() < button.getP2().getX()) and (pClick.getY() < button.getP2().getY()):
        return True

#This function Displays the score
def statDisplay(win):
    #score = calcScore(score)
    #direction = getDirection(direction)
    #success = getSuccess(success)
    scoreDisplay = Text(Point(Xmin+100,Ymin+50), "SCORE").draw(win)
    moveSuccess = Text(Point(Xmin+250,Ymin+50), "Move DIRECTION is SUCCESS").draw(win)

#This function initialises the gamestate, putting 0 and 2 in random squares
def newGamestate():
    matrix = [[0]*5 for i in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            rand = random.randint(0, 1)
            if rand == 1:
                box = Box()
                setattr(box, "value",2)
                matrix[i][j] = Box()
    return matrix
#Moves tiles left
def left(matrix):
    for i in range(0,5):
        k=0
        leftRow = [0,0,0,0,0]
        initialRow = [0,0,0,0,0]
        for j in range(0,5):
            if(matrix[i][j] != 0):
                initialRow[j] = matrix[i][j] #creates alias of column
                leftRow[k] = matrix[i][j] #creates column shifted up
                k = k+1
        for j in range(0,4):
            if leftRow[j] == leftRow[j+1] and leftRow[j]!=0:
                x = leftRow[j];
                leftRow[j] = x*2
                leftRow[j+1] = 0
            if upColumn[j] == upColumn[j+1] and upColumn[j]!=0:
                x = upColumn[j];
                upColumn[j] = x*2
                upColumn[j+1] = 0
<<<<<<< HEAD

=======
>>>>>>> 1e84b181d65608f3c786dcc0b6c531557de1c84a
        k = 0
        for j in range(0,5):
            matrix[i][j] = 0
            if leftRow[j] != 0:
                matrix[i][j] = leftRow[j]
                k = k + 1
<<<<<<< HEAD

=======
>>>>>>> 1e84b181d65608f3c786dcc0b6c531557de1c84a
    return matrix

#rotates matrix clockwise 90 degrees
def clockwise(matrix):
    rotatedMatrix = [[0]*5 for i in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            rotatedMatrix[i][j] = matrix[5-j-1][i]
    return rotatedMatrix
<<<<<<< HEAD


    
=======
    return matrix
>>>>>>> 1e84b181d65608f3c786dcc0b6c531557de1c84a
    
main()
