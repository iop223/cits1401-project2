class box(object):
    coordinate = 0
    value = 0
    highlight = 0
    colour = (255,0,255)
    def __init__(coordinate,value,highlight):
        self.xY = xY
        self.value = value
        self.highlight = highlight
        self.colour = colour

    def makeBox(coordinate,value,highlight):
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
    
    def determineHighlight(highlight):
        colourTemp = (255,0,255)
        if highlight == 1:
                colourTemp = (188,0,255)
        return colourTemp

    
