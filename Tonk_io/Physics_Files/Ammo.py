try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constants are written in capital letters
IMG = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/ammo.png')

# The Enemy class
class Ammo:
    
    # Initialiser
    def __init__(self, pos):
        self.pos = pos
        self.img_dest_dim = (64,64)
        self.radius = 32
    
    # Draws the enemy object
    def draw(self, canvas):
        canvas.draw_image(IMG, (64, 64), (128, 128), self.pos.get_p(), self.img_dest_dim)
    
    # Checks if the enemy has hit something
    def hit(self, item):
        distance = item.pos.copy().subtract(self.pos).length()
        return distance < item.getRadius() + self.getRadius()
    
    # Returns position
    def getPos(self):
        return self.pos
    
    # Returns velocity
    def getVel(self):
        return self.vel
    
    # Returns radius  
    def getRadius(self):
        return self.radius