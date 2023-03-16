# The Rocket Class
class Rocket:
    
    # Initialiser
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 6

    # Draws the rocket object
    def drawRocket(self, canvas):
        canvas.draw_circle([int(self.pos.get_p()[0]), int(self.pos.get_p()[1])], self.radius, 2, "Black", "Red")

    # Updates the rockets position using its velocity
    def update(self):
        self.pos.add(self.vel)
    
    # Returns position
    def getPos(self):
        return self.pos
    
    # Returns velocity
    def getVel(self):
        return self.vel
    
    # Returns radius
    def getRadius(self):
        return self.radius