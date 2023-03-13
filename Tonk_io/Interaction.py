try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
import random
from Physics_Files.Vector import Vector
from Physics_Files.Rocket import Rocket
from Physics_Files.Enemy import Enemy

# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720

class Interaction:

    # Initialiser
    def __init__(self, tonk, kbd, mouse):
        self.tonk = tonk
        self.kbd = kbd
        self.mouse = mouse
        
        self.rocketList = []
        self.enemyList = []
        
        self.score = 0
        self.lives = 3
        self.fireRate = 20

    # Updates player position
    def updateTonk(self, canvas):
        if(self.kbd.up and self.tonk.pos.get_p()[1]-52 > 0):
            self.tonk.vel.add(Vector(0,-1))
        if(self.kbd.left and self.tonk.pos.get_p()[0]-52 > 0):
            self.tonk.vel.add(Vector(-1, 0))
        if(self.kbd.down and self.tonk.pos.get_p()[1]+52 < HEIGHT):
            self.tonk.vel.add(Vector(0,1))
        if(self.kbd.right and self.tonk.pos.get_p()[0]+52 < WIDTH):
            self.tonk.vel.add(Vector(1, 0))
        
        self.tonk.draw(canvas)
        self.tonk.update()
        
    # Creates rockets if mouse clicked
    def updateRockets(self, canvas):
        mousePos = self.mouse.mousePos()
        
        if(mousePos != None):
            relX = mousePos[0] - self.tonk.pos.get_p()[0]
            relY = mousePos[1] - self.tonk.pos.get_p()[1]
            self.tonk.img_rot = math.atan2(relY, relX)
            
        
            rocketPos = self.tonk.pos.copy().add(Vector(relX, relY).normalize().multiply(40))
            rocketVel = Vector(relX, relY).normalize().multiply(10).add(self.tonk.vel.copy())
            self.rocketList.append(Rocket(rocketPos, rocketVel))
        
        for rocket in self.rocketList:
            rocket.drawRocket(canvas)
            rocket.update()
        
        doNotRemove = []
        for rocket in self.rocketList:
            if(rocket.pos.get_p()[0] > 0 and rocket.pos.get_p()[0] < 1280 and rocket.pos.get_p()[1] > 0 and rocket.pos.get_p()[1] < 720):
                doNotRemove.append(rocket)
                
        self.rocketList.clear()
        self.rocketList = doNotRemove
    
    # Updates enemy positions
    def updateEnemies(self, canvas):
        for enemy in self.enemyList:
            enemy.draw(canvas)
            enemy.update()
        
        doNotRemove = []
        for enemy in self.enemyList:
            if(enemy.pos.get_p()[0] > -10 and enemy.pos.get_p()[0] < 1290 and enemy.pos.get_p()[1] > -10 and enemy.pos.get_p()[1] < 730):
                doNotRemove.append(enemy)
                
        self.enemyList.clear()
        self.enemyList = doNotRemove
            
    # Checks if a rocket has hit an enemy
    def updateCollisions(self):
        for rocket in self.rocketList:
            for enemy in self.enemyList:
                if enemy.hit(rocket):
                    self.collide(self.rocketList.index(rocket), self.enemyList.index(enemy))
     
    # If a collision happens between a rocket and an enemy, it removes them from the respective lists    
    def collide(self, rocket, enemy):
        self.score = self.score + 1
        self.rocketList.pop(rocket)
        self.enemyList.pop(enemy)  
        
    # Checks if an enemy hits the player
    def playerHit(self):
        for enemy in self.enemyList:
                if enemy.hit(self.tonk):
                    self.lives = self.lives - 1
                    self.enemyList.pop(self.enemyList.index(enemy))
                    
    # Creates enemies
    def timer_handler(self):
        enemyPos = self.randPos()
        enemyVel = self.vel(enemyPos)
        enemy = Enemy(enemyPos, enemyVel)
        self.enemyList.append(enemy)
    
    # Gets a random position for the enemy to spawn
    def randPos(self):
        axis = random.randrange (1, 4)
        
        if(axis == 1):
            return Vector(random.randrange (0, 1280), -10)
        elif(axis == 2):
            return Vector(random.randrange (0, 1280), 730)
        elif(axis == 3):
            return Vector(-10, random.randrange (0, 720))
        else:
            return Vector(1290, random.randrange (0, 720))

    # Calculates the enemies velocity to point at the player when it spawns
    def vel(self, pos):
        relX =  self.tonk.pos.get_p()[0] - pos.get_p()[0]
        relY = self.tonk.pos.get_p()[1] - pos.get_p()[1]
        return Vector(relX, relY).normalize().multiply(6)