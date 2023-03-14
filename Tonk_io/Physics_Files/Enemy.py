try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# The Enemy class
class Enemy:
    
    # Initialiser
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 20
    
    # Draws the enemy object
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 2, "Black", "Blue") 
    
    # Updates the enemies position using its velocity  
    def update(self):
        self.pos.add(self.vel)
    
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