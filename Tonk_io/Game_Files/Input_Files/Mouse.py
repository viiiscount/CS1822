try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# The Mouse Class
class Mouse:
    def __init__(self, position=None):
        self.pos = position

    def mouse_handler(self, position):
        self.pos = position
    
    def click_pos(self):
        temp = self.pos
        self.pos = None
        return temp