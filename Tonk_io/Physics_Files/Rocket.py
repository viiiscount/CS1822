try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from .Vector import Vector

# The Rocket Class
class Rocket:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def drawRocket(self, canvas):
        canvas.draw_circle([int(self.pos.get_p()[0]), int(self.pos.get_p()[1])], 6, 2, "Black", "Red")

    def update(self):
        self.pos.add(self.vel)

    def getPosX(self):
        return int(self.pos.get_p()[0])
    
    def getPosY(self):
        return int(self.pos.get_p()[1])
    
    def getRadius(self):
        return 8