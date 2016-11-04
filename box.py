from graphics import *
value = 0
highlight = 0
class Box:
    def __init__(self,value=0,highlight=0):
        self.value = value
        self.highlight = highlight
        
    def makeBox(value,highlight):
        box = Box()
        box.value = value
        box.highlight = highlight
        return box
