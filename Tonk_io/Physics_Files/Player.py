try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from .Vector import Vector

# Constants are written in capital letters
IMG = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/tank.png')

# The Player class
class Player:
    
    # Initialiser
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pos = Vector(width/2, height/2)
        self.vel = Vector()
        self.img_dest_dim = (128,128)
        self.img_rot = 0
        self.speed_multiplier = 0.75
        self.radius = 35

    # Draws the player
    def draw(self, canvas):
        canvas.draw_image(IMG, (64, 64), (128, 128), self.pos.get_p(), self.img_dest_dim, self.img_rot)
    
    # Updates the players position using its velocity, and prevents the player from going outside of the arena    
    def update(self):
        self.pos.add(self.vel)
        
        if(self.pos.get_p()[1]-52 < 0):
            self.vel.y = 0
        if(self.pos.get_p()[0]-52 < 0):
            self.vel.x = 0
        if(self.pos.get_p()[1]+52 > self.height):
            self.vel.y = 0
        if(self.pos.get_p()[0]+52 > self.width):
            self.vel.x = 0
            
        # Changes the speed using the speed multiplier
        self.vel.multiply(self.speed_multiplier)
    
    # Returns position
    def getPos(self):
        return self.pos
    
    # Returns velocity
    def getVel(self):
        return self.vel
    
    # Returns radius  
    def getRadius(self):
        return self.radius