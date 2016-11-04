from graphics import *
listNum = 0
value = 0
highlight = 0
class Box:
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

    def setListNum(inListNum):
        listNum = inListNum
    
    def getValue():
        return value
    
    def getListNum():
        return listNum

    def getHighlight():
        x=highlight
        return x
