try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from .Vector import Vector

# The Rocket Class
class Rocket:
    
    # Initialiser
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 8

    # Draws the rocket object
    def drawRocket(self, canvas):
        canvas.draw_circle([int(self.pos.get_p()[0]), int(self.pos.get_p()[1])], self.radius, 1, "Black", "Red")

    # Updates the rockets position using its velocity
    def update(self):
        self.pos.add(self.vel)
    
    # Returns rocket radius
    def getRadius(self):
        return self.radius