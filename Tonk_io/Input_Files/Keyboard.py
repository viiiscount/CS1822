try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
 
# The Keyboard Class   
class Keyboard:
    
    # Initialiser
    def __init__(self):
        self.up = False
        self.left = False
        self.down = False
        self.right = False
        
    # Handles key down presses
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['d']:
            self.right = True

    # Handles key up presses
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP['d']:
            self.right = False