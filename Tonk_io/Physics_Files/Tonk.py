try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from .Vector import Vector

# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720
IMG = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/Tonk.png')
IMG_CENTRE = (50, 50)
IMG_DIMS = (100, 100)

class Tonk:
    
    # Initialiser
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector()
        self.img_dest_dim = (100,100)
        self.img_rot = 0
        self.speed_multiplier = 0.75
        self.radius = 40

    # Draws the player
    def draw(self, canvas):
        canvas.draw_image(IMG, IMG_CENTRE, IMG_DIMS, self.pos.get_p(), self.img_dest_dim, self.img_rot)
    
    # Updates the players position using its velocity, and prevents the player from going outside of the arena    
    def update(self):
        self.pos.add(self.vel)
        
        if(self.pos.get_p()[1]-52 < 0):
            self.vel.y = 0
        if(self.pos.get_p()[0]-52 < 0):
            self.vel.x = 0
        if(self.pos.get_p()[1]+52 > HEIGHT):
            self.vel.y = 0
        if(self.pos.get_p()[0]+52 > WIDTH):
            self.vel.x = 0
            
        # Changes the speed using the speed multiplier
        self.vel.multiply(self.speed_multiplier)
    
    # Returns radius  
    def getRadius(self):
        return self.radius