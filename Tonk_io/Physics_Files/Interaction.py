# The Interaction class
class Interaction: 

    # Checks if a rocket has hit an enemy
    def rocketCollision(self, rocketList, enemyList, score):
        for rocket in rocketList:
            for enemy in enemyList:
                if(enemy.hit(rocket)):
                    score = score + 1
                    rocketList.pop(rocketList.index(rocket))
                    enemyList.pop(enemyList.index(enemy))
                    
        return rocketList, enemyList, score
    
    # Checks if an enemy hits the player
    def playerCollision(self, enemyList, player, lives):
        for enemy in enemyList:
                if enemy.hit(player):
                    lives = lives - 1
                    enemyList.pop(enemyList.index(enemy))
        
        return enemyList, player, lives