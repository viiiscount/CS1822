# The Interaction class
class Interaction: 

    # Checks if a rocket has hit an enemy
    def rocketCollision(self, rocketList, enemyList, score):
        for rocket in rocketList:
            for enemy in enemyList:
                if(enemy.hit(rocket)):
                    score = score + 1
                    rocketList.pop(rocketList.index(rocket))
                    explosion(enemyList.index(enemy)) = Spritesheet(https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/dominic-garcia-tumblr-ojn6bb7cfk1w36evao1-1280.jpg, 3, 5, 16, enemy.pos.get_p(x), enemy.pos.get_p(y), 20)
                    explosions.append(explosion(enemyList.index(enemy)))
                    enemyList.pop(enemyList.index(enemy))
                    
        return rocketList, enemyList, score
    
    # Checks if an enemy hits the player
    def playerCollision(self, enemyList, player, lives):
        for enemy in enemyList:
                if enemy.hit(player):
                    lives = lives - 1
                    enemyList.pop(enemyList.index(enemy))
        
        return enemyList, player, lives
