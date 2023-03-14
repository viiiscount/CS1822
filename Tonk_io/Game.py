try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
import random
from Physics_Files.Vector import Vector
from Physics_Files.Player import Player
from Physics_Files.Enemy import Enemy
from Physics_Files.Rocket import Rocket
from Physics_Files.Interaction import Interaction

# The Game Wrapper class
class Game:
    
    # Initialiser
    def __init__(self, kbd, mouse, width, height):
        self.kbd = kbd
        self.mouse = mouse
        self.width = width
        self.height = height
        self.player = Player(width, height)
        self.interaction = Interaction()
        self.rocketList = []
        self.enemyList = []
        self.score = 0
        self.lives = 3
        
    # Runs the game loop
    def gameLoop(self, canvas):
        self.updateEnemies(canvas)
        self.updateRockets(canvas)
        self.updatePlayer(canvas)
        self.rocketList, self.enemyList, self.score = self.interaction.rocketCollision(self.rocketList, self.enemyList, self.score)
        self.enemyList, self.player, self.lives = self.interaction.playerCollision(self.enemyList, self.player, self.lives)
        canvas.draw_text("Lives: " + str(self.lives), (10, 25), 25, 'Black', 'monospace')
        canvas.draw_text("Score: " + str(self.score), (150, 25), 25, 'Black', 'monospace')
    
    # Resets the game   
    def reset(self):
        self.player = Player(self.width, self.height)
        self.rocketList = []
        self.enemyList = []
        self.score = 0
        self.lives = 3
        self.fireRate = 2000
        
    # Updates player position
    def updatePlayer(self, canvas):
        if(self.kbd.up and self.player.getPos().get_p()[1]-52 > 0):
            self.player.vel.add(Vector(0,-1))
        if(self.kbd.left and self.player.getPos().get_p()[0]-52 > 0):
            self.player.vel.add(Vector(-1, 0))
        if(self.kbd.down and self.player.getPos().get_p()[1]+52 < self.height):
            self.player.vel.add(Vector(0,1))
        if(self.kbd.right and self.player.getPos().get_p()[0]+52 < self.width):
            self.player.vel.add(Vector(1, 0))
        
        self.player.draw(canvas)
        self.player.update()
        
    # Creates rockets if mouse clicked
    def updateRockets(self, canvas):
        self.rocketList = self.inBounds(self.rocketList)
        mousePos = self.mouse.getPos()         
        
        if(mousePos != None):
            relX = mousePos[0] - self.player.getPos().get_p()[0]
            relY = mousePos[1] - self.player.getPos().get_p()[1]
            self.player.img_rot = math.atan2(relY, relX)
            rocketPos = self.player.getPos().copy().add(Vector(relX, relY).normalize().multiply(40))
            rocketVel = Vector(relX, relY).normalize().multiply(10).add(self.player.getVel().copy())
            self.rocketList.append(Rocket(rocketPos, rocketVel))

        for rocket in self.rocketList:
            rocket.drawRocket(canvas)
            rocket.update()
    
    # Updates enemy positions
    def updateEnemies(self, canvas):        
        for enemy in self.enemyList:
            enemy.draw(canvas)
            enemy.update()    
               
        self.enemyList = self.inBounds(self.enemyList)
    
    # Checks if item is in the arena
    def inBounds(self, removeList):
        doNotRemove = []
        
        for item in removeList:
            if(item.getPos().get_p()[0] > -10 and item.getPos().get_p()[0] < 1290 and item.getPos().get_p()[1] > -10 and item.getPos().get_p()[1] < 730):
                doNotRemove.append(item)
        
        return doNotRemove
        
        
    # Creates enemies
    def timer_handler(self):
        enemyPos = self.randPos()
        enemyVel = self.vel(enemyPos)
        enemy = Enemy(enemyPos, enemyVel)
        self.enemyList.append(enemy)
    
    # Gets a random position for the enemy to spawn
    def randPos(self):
        axis = random.randrange(1, 4)
        
        if(axis == 1):
            return Vector(random.randrange(0, 1280), -10)
        elif(axis == 2):
            return Vector(random.randrange(0, 1280), 730)
        elif(axis == 3):
            return Vector(-10, random.randrange(0, 720))
        else:
            return Vector(1290, random.randrange(0, 720))

    # Calculates the enemies velocity to point at the player when it spawns
    def vel(self, pos):
        relX =  self.player.getPos().get_p()[0] - pos.get_p()[0]
        relY = self.player.getPos().get_p()[1] - pos.get_p()[1]
        return Vector(relX, relY).normalize().multiply(6)