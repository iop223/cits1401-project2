from graphics import *
class Box(object):
    coordinate = Rectangle(Point(0,0),Point(0,0))
    value = 0
    highlight = 0
    colour = (255,0,255)
    
    def __init__(self,coordinate,value,highlight):
        self.coordinate = coordinate
        self.value = value
        self.highlight = highlight
        self.colour = colour
        
    def setBox(coordinate,value,highlight):
        box = Box()
        box.coordinate = coordinate
        box.value = value
        box.highlight = highlight
        box.colour = determineHighlight(highlight)
        return box
    
    def setValue(value):
        box.value = value

    def setCoordinate(coordinate):
        box.coordiante = coordinate

    def setColour(highlight):
        box.colour = determineHighlight(highlight)

    def getBox():
        return box

    def getValue():
        return value
    
    def getColour():
        return colour

    def getCoordinate():
        return coordinate

    def getMidpoint(coordiante):
        midpointX = (coordinate.getP1().getX() + coordinate.getP2().getX())/2
        midpointY = (coordinate.getP1().getY() + coordinate.getP2().getY())/2
        midpoint = Point(midpointX,midpointY)
        return midpoint
    
    def determineHighlight(highlight):
        colourTemp = setFill(color_rgb(255,0,255))
        if highlight == 1:
                colourTemp = setFill(color_rgb(188,0,255))
        return colourTemp

    def drawBox():
        box = box.getCoordiante()
        box.setFill(colour_rgb(box.getColour()))
        return box

