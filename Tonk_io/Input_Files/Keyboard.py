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
        self.fire = False
        self.pause = False

    # Handles key down
    def keyDown(self, key):
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['space']:
            self.fire = True
        if key == simplegui.KEY_MAP['p']:
            self.pause = True

    # Handles key up
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['space']:
            self.fire = False
        if key == simplegui.KEY_MAP['p']:
            self.pause = False