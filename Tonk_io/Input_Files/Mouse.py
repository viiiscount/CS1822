try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# The Mouse Class
class Mouse:
    
    # Initialiser
    def __init__(self, position=None):
        self.pos = position

    # Gets mouse position when mouse clicked
    def mouse_handler(self, position):
        self.pos = position
        
    # Returns mouse position annd sets position to None
    def getPos(self):
        temp = self.pos
        self.pos = None
        return temp
    
    