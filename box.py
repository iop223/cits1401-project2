from graphics import *
class Box(object):
    shape = Rectangle(Point(0,0),Point(0,0))
    value = 0.0
    highlight = 0
    
    def __init__(shape, value , highlight):
        self.shape = shape
        self.value = value
        self.highlight = value
        
    def makeBox(shape,value,highlight):
        box = Box()
        box.shape = shape
        box.value = value
        box.highlight = highlight
        determineHighlight(highlight,shape)
        return box

    def setShape(shape):
        box.shape = shape

    def setColour(highlight):
        box.highlight = highlight
        determineHighlight(highlight,shape)

    def getMidpoint(shape):
        midpointX = (shape.getP1().getX() + shape.getP2().getX())/2
        midpointY = (shape.getP1().getY() + shape.getP2().getY())/2
        midpoint = Point(midpointX,midpointY)
        return midpoint
    
    def determineHighlight(highlight,rectangle):
        colourTemp = shape.setFill(color_rgb(255,0,255))
        if highlight == 1:
                colourTemp = shape.setFill(color_rgb(188,0,255))
        return colourTemp

    def drawShape(shape):
        return shape


