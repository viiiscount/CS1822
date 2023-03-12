try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
from Physics_Files.Vector import Vector
from Physics_Files.Rocket import Rocket

# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720

class Interaction:
    def __init__(self, tonk, kbd, mouse):
        self.tonk = tonk
        self.kbd = kbd
        self.mouse = mouse
        self.rocketList = []
        self.counter = 0
        self.fireRate = 20

    def updateTonk(self):
        if(self.kbd.up and self.tonk.pos.get_p()[1]-52 > 0):
            self.tonk.vel.add(Vector(0,-1))
        if(self.kbd.left and self.tonk.pos.get_p()[0]-52 > 0):
            self.tonk.vel.add(Vector(-1, 0))
        if(self.kbd.down and self.tonk.pos.get_p()[1]+52 < HEIGHT):
            self.tonk.vel.add(Vector(0,1))
        if(self.kbd.right and self.tonk.pos.get_p()[0]+52 < WIDTH):
            self.tonk.vel.add(Vector(1, 0))
        
    def updateRockets(self, canvas):
        
        mousePos = self.mouse.mouse_moved()
        
        if(mousePos != None):
            
            relX = mousePos[0] - self.tonk.pos.get_p()[0]
            relY = mousePos[1] - self.tonk.pos.get_p()[1]
            self.tonk.img_rot = math.atan2(relY, relX)
            
            if(self.counter % self.fireRate == 0):
                
                rocketPos = self.tonk.pos.copy().add(Vector(relX, relY).normalize().multiply(40))
                rocketVel = Vector(relX, relY).normalize().multiply(10).add(self.tonk.vel.copy())
                self.rocketList.append(Rocket(rocketPos, rocketVel))
        
        for rocket in self.rocketList:
            rocket.drawRocket(canvas)
            rocket.update()
        
        doNotRemove = []
        
        for rocket in self.rocketList:
            if(rocket.getPosY() > 0 and rocket.getPosY() < 720 and rocket.getPosX() > 0 and rocket.getPosX() < 1280):
                doNotRemove.append(rocket)
                
        self.rocketList.clear()
        self.rocketList = doNotRemove
        self.counter = self.counter + 1