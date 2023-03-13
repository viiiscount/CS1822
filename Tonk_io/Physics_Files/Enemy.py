try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
from .Vector import Vector

class Enemy:
    
    # Initialiser
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 20
    
    # Draws the enemy object
    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(), self.radius, 1, "Black", "Blue") 
    
    # Updates the enemies position using its velocity  
    def update(self):
        self.pos.add(self.vel)
    
    # Returns enemy radius  
    def getRadius(self):
        return self.radius
    
    # Checks if the enemy has hit something
    def hit(self, item):
        distance = item.pos.copy().subtract(self.pos).length()
        return distance < item.getRadius() + self.getRadius()