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
from Physics_Files.Ammo import Ammo
from Physics_Files.Interaction import Interaction
from Physics_Files.Spritesheet import Clock

# Constants are written in capital letters
IMG = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/score.png')
IMG2 = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/health.png')
IMG3 = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/ammo.png')

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
        self.timer = Clock()
        
        self.rocketList = []
        self.enemyList = []
        self.explosionList = []
        self.ammoList = []
        
        self.score = 0
        self.lives = 0
        self.ammo = 0
        
    # Runs the game loop
    def gameLoop(self, canvas):
        self.updateAmmo(canvas)
        self.updateEnemies(canvas)
        self.updateRockets(canvas)
        self.updatePlayer(canvas)
        self.updateExplosions(canvas)
        self.rocketList, self.enemyList, self.explosionList, self.score, self.ammo = self.interaction.rocketCollision(self.rocketList, self.enemyList, self.explosionList, self.score, self.ammo)
        self.ammoList, self.player, self.ammo = self.interaction.ammoCollision(self.ammoList, self.player, self.ammo)
        self.enemyList, self.player, self.lives = self.interaction.playerCollision(self.enemyList, self.player, self.lives)
        canvas.draw_image(IMG, (64, 64), (128, 128), (40,40), (64, 64))
        canvas.draw_image(IMG2, (64, 64), (128, 128), (40,110), (64, 64))
        canvas.draw_image(IMG3, (64, 64), (128, 128), (40,180), (64, 64))
        canvas.draw_text(str(self.score), (85, 50), 40, 'Black', 'sans-serif')
        canvas.draw_text(str(self.lives), (85, 120), 40, 'Black', 'sans-serif')
        canvas.draw_text(str(self.ammo), (85, 190), 40, 'Black', 'sans-serif')
    
    # Resets the game   
    def reset(self):
        self.player = Player(self.width, self.height)
        self.rocketList = []
        self.enemyList = []
        self.explosionList = []
        self.ammoList = []
        self.score = 0
        self.lives = 3
        self.ammo = 25

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
            if(self.ammo != 0):
                rocketPos = self.player.getPos().copy().add(Vector(relX, relY).normalize().multiply(40))
                rocketVel = Vector(relX, relY).normalize().multiply(10).add(self.player.getVel().copy())
                self.rocketList.append(Rocket(rocketPos, rocketVel))
                self.ammo = self.ammo - 1

        for rocket in self.rocketList:
            rocket.drawRocket(canvas)
            rocket.update()
    
    # Updates enemy positions
    def updateEnemies(self, canvas):        
        for enemy in self.enemyList:
            enemy.draw(canvas)
            enemy.update()    
               
        self.enemyList = self.inBounds(self.enemyList)
    
    # Draws ammo
    def updateAmmo(self, canvas):
        for item in self.ammoList:
            item.draw(canvas)
        
    # Draws explosions 
    def updateExplosions(self, canvas):
        doNotRemove = []
                
        self.timer.tick()
        for item in self.explosionList: 
            item.draw(canvas)
            if(self.timer.transition(2) == True and item.done() == False):
                item.next_frame()
                
            if(item.done() == False):
                doNotRemove.append(item)
        
        self.explosionList = doNotRemove 
    
    # Checks if item is in the arena
    def inBounds(self, removeList):
        doNotRemove = []
        
        for item in removeList:
            if(item.getPos().get_p()[0] > -10 and item.getPos().get_p()[0] < 1290 and item.getPos().get_p()[1] > -10 and item.getPos().get_p()[1] < 730):
                doNotRemove.append(item)
        
        return doNotRemove
        
    def powerupTimer(self):
        rand = random.randrange(1, 5)
        if(rand == 5):
            ammo = Ammo((Vector(random.randrange(100, 1250), random.randrange(30, 690))))
            self.ammoList.append(ammo)

    # Creates enemies
    def enemyTimer(self):
        enemyPos = self.randEnemyPos()
        enemyVel, enemyRot = self.vel(enemyPos)
        enemy = Enemy(enemyPos, enemyVel, enemyRot)
        self.enemyList.append(enemy)
    
    # Gets a random position for the enemy to spawn
    def randEnemyPos(self):
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
        return Vector(relX, relY).normalize().multiply(6), math.atan2(relY, relX)                