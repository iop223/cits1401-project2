## Justin Chong 21508335, Mitchell Wooding 22088045

from graphics import *
import math
import random
Xmin, Xmax = 0, 720
Ymin, Ymax = 0, 720
score = 0
gameState = [[0]*5 for i in range(5)]
highlightState = [[0]*5 for i in range(5)]
moveDirection = "foobar"
#This function is the main control of the flow of the program
def main():
    global moveDirection
    legalMove = False
    win = GraphWin('wewuz', Xmax-Xmin, Ymax-Ymin)    
    win.setCoords(Xmin, Ymin, Xmax, Ymax)
    quitButton, newGamebutton, upButton, downButton, leftButton, rightButton, upBorder, downBorder, leftBorder, rightBorder = makeInterface(win)
    x = 0
    global score
    global gameState
    gameState = newGamestate()
    oldGameState = newGamestate()
    while x==0:
        Pt = win.getMouse()
        if isClicked(Pt,quitButton):
            win.close()
        elif isClicked(Pt,newGamebutton):
            print ("Create new game")
            gameState = newGamestate()
            score = 0
            computerPlayer()
        elif isClicked(Pt,upButton) or isClicked(Pt,upBorder):
            moveDirection = "UP"
            doMove(0) #moves up
        elif isClicked(Pt,downButton) or isClicked(Pt,downBorder):
            moveDirection = "DOWN"
            doMove(1) #moves down
        elif isClicked(Pt,leftButton) or isClicked(Pt,leftBorder):
            moveDirection = "LEFT"
            doMove(2) #moves left
        elif isClicked(Pt,rightButton) or isClicked(Pt,rightBorder):
            moveDirection = "RIGHT"
            doMove(3) #moves right
        oldGameState=compareHighlight(oldGameState)
        drawboxes(win)
        statDisplay(win)
            
def erase(win):
    rect = Rectangle(Point(Xmin,Ymin), Point(Xmax,Ymax))
    rect.setFill(color_rgb(139,69,19))
    rect.draw(win)
    
def drawboxes(win):
    x=0
    for i in range(0,5):
        for j in range(0,5):
            square = Rectangle(Point(Xmin+5+i*100,Ymax-5-j*100), Point(Xmin+100+i*100,Ymax-100-j*100))
            square.setFill(color_rgb(255,0,255))
            if highlightState[j][i]==1:
                square.setFill(color_rgb(0,255,0))
            square.draw(win)
            if gameState[j][i] >= 2:
                Text(Point(Xmin+52.5+i*100, Ymax-52.5-j*100),gameState[j][i]).draw(win)
            x=x+1

def compareHighlight(oldGameState):
    global gameState
    global highlightState
    for i in range(0,5):
        for j in range(0,5):
            highlightState[j][i] = 0
            if (gameState[j][i] != oldGameState[j][i]) and gameState[j][i] != 0:
                highlightState[j][i] = 1
    oldGameState=gameState
    return oldGameState
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
    global score
    global moveDirection
    statBar = Rectangle(Point(Xmin, Ymin),Point(Xmax-300,Ymin+200))
    statBar.setFill(color_rgb(139,69,19))
    statBar.setOutline(color_rgb(139,69,19))
    statBar.draw(win)
    scoreDisplay = Text(Point(Xmin+100,Ymin+50), score).draw(win)
    moveSuccess = Text(Point(Xmin+250,Ymin+50), "Move DIRECTION is %s" % moveDirection).draw(win)

#This function initialises the gamestate, putting 0 and 2 in random squares
def newGamestate():
    matrix = [[0]*5 for i in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            rand = random.randint(0, 1)
            if rand == 1:
                matrix[i][j] = 2
    return matrix
#Moves tiles left
def left(matrix):
    global score
    global highlightState
    merged = False
    for i in range(0,5):
        k=0
        leftRow = [0,0,0,0,0]
        initialRow = [0,0,0,0,0]
        for j in range(0,5):
            if(matrix[i][j] != 0):
                initialRow[j] = matrix[i][j] #creates alias of column
                leftRow[k] = matrix[i][j] #creates column shifted left
                k = k+1
        for j in range(0,4):
            if leftRow[j] == leftRow[j+1] and leftRow[j]!=0: # if adjacent tile is equal, merge
                x = leftRow[j];
                leftRow[j] = x*2
                leftRow[j+1] = 0
                merged = True
        k = 0
        for j in range(0,5):
            matrix[i][j] = 0
            if leftRow[j] != 0:
                matrix[i][j] = leftRow[j]
                k = k + 1
    if merged:
        score = score + 1
    return matrix
def doMove(direction): #moves the gamestate, counts score etc
    global gameState
    global score
    initialMatrix = [[0]*5 for i in range(5)]
    initialMatrix = gameState
    print("before")
    print(initialMatrix)
    if direction == 0:
        gameState = up(gameState)
        print(initialMatrix)
        print("are they equal")
        print(gameState)
    elif direction == 1:
        gameState = down(gameState)
        print(initialMatrix)
        print("are they equal")
        print(gameState)
    elif direction == 2:
        gameState = clockwise(gameState)
        gameState = up(gameState)
        gameState = antiClockwise(gameState)
        print("after")
        print(initialMatrix)
    elif direction == 3:
        gameState = right(gameState)
        print(initialMatrix)
        print("are they equal")
        print(gameState)
        
    if gameState != initialMatrix:
        print("kill yourself")
        legalMove = True
        gameState[findZero(gameState)[0]][findZero(gameState)[1]] = 2
    else:
        legalMove = False
        score = score-1
        print (legalMove)
        print (score)
    if gameOver(gameState):
        print("GAME OVER")

#rotates matrix clockwise 90 degrees
def clockwise(matrix):
    rotatedMatrix = [[0]*5 for i in range(5)]
    for i in range(0,5):
        for j in range(0,5):
            rotatedMatrix[i][j] = matrix[5-j-1][i]
    return rotatedMatrix
#rotates matrix clockwise 90 degrees
def antiClockwise(matrix):
    return clockwise(clockwise(clockwise(matrix)))
#Moves tiles up
def up(matrix):
    matrix = antiClockwise(matrix)
    matrix = left(matrix)
    matrix = clockwise(matrix)
    return matrix
#Move tiles down
def down(matrix):
    matrix = clockwise(matrix)
    matrix = left(matrix)
    matrix = antiClockwise(matrix)
    return matrix
#move tiles right
def right(matrix):
    matrix = clockwise(clockwise(matrix))
    matrix = left(matrix)
    matrix = clockwise(clockwise(matrix))
    return matrix
#gameOver boolean
def gameOver(matrix):
    isFull = True
    gameOver = True
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] == 0:
                isFull = False
                gameOver = False
    if isFull:
        for i in range(0,4):
            for j in range(0,4):
                if matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1]:
                    gameOver = False
    return gameOver
#finds the bottom right tile to spawn the 2 square
def findZero(matrix):
    coordinate = [0,0]
    for i in range(4,-1,-1):
        for j in range(4,-1,-1):
            if matrix[i][j] ==0:
                coordinate[0] = i
                coordinate[1] = j
                return coordinate
    return coordinate

def computerPlayer():
    global gameState
    while 0==0:
        rand = random.randint(0, 3)
        doMove(rand)
        print(gameState)
        if gameOver(gameState):
            break
main()
