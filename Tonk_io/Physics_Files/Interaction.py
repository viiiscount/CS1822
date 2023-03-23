from .Spritesheet import Spritesheet

# The Interaction class
class Interaction: 
        
    # Checks if a rocket has hit an enemy
    def rocketCollision(self, rocketList, enemyList, explosionList, score, ammo):
        for rocket in rocketList:
            for enemy in enemyList:
                if(enemy.hit(rocket)):
                    score = score + 1
                    ammo = ammo + 3
                    rocketList.pop(rocketList.index(rocket))
                    explosion = Spritesheet(enemy.pos.get_p()[0], enemy.pos.get_p()[1])
                    explosionList.append(explosion)
                    enemyList.pop(enemyList.index(enemy))
                    
        return rocketList, enemyList, explosionList, score, ammo
    
    def ammoCollision(self, ammoList, player, ammo):
        for item in ammoList:
                if item.hit(player):
                    ammo = ammo + 10
                    ammoList.pop(ammoList.index(item))
        
        return ammoList, player, ammo
    
    # Checks if an enemy hits the player
    def playerCollision(self, enemyList, player, lives):
        for enemy in enemyList:
                if enemy.hit(player):
                    lives = lives - 1
                    enemyList.pop(enemyList.index(enemy))
        
        return enemyList, player, lives
