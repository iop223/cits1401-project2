from graphics import *
listNum = 0
value = 0
highlight = 0
class Box:
    pass
    def __init__(self,listNum=0,value=0,highlight=0):
        self.listNum = listNum
        self.value = value
        self.highlight = highlight
        
    def makeBox(listNum,value,highlight):
        box = Box()
        box.listNum
        box.value = value
        box.highlight = highlight
        return box

    def setHighlight(highlight):
        box = Box()
        box.highlight=highlight
        return box

    def setValue(value):
        box = Box()
        box.value=value
        return box

    def setListNum(listNum):
        box = Box()
        box.listNum=listNum
        return box
    
    def getValue():
        return value
    
    def getListNum():
        return listNum

    def getHighlight(highlight):
        if highlight == 1:
            isHighlight = True
        else:
            isHighlight = False
        return highlight
