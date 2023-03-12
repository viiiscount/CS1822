try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
from Physics_Files.Vector import Vector

# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720

class Interaction:
    def __init__(self, tonk, kbd, mouse):
        self.tonk = tonk
        self.kbd = kbd
        self.mouse = mouse

    def update(self):
        mousePos = self.mouse.click_pos()
        if(mousePos != None):
            posX = mousePos[0] - self.tonk.pos.get_p()[0]
            posY = mousePos[1] - self.tonk.pos.get_p()[1]
            self.tonk.img_rot = math.atan2(posY, posX)
        
        if(self.kbd.up and self.tonk.pos.get_p()[1]-52 > 0):
            self.tonk.vel.add(Vector(0,-1))
        if(self.kbd.left and self.tonk.pos.get_p()[0]-52 > 0):
            self.tonk.vel.add(Vector(-1, 0))
        if(self.kbd.down and self.tonk.pos.get_p()[1]+52 < HEIGHT):
            self.tonk.vel.add(Vector(0,1))
        if(self.kbd.right and self.tonk.pos.get_p()[0]+52 < WIDTH):
            self.tonk.vel.add(Vector(1, 0))