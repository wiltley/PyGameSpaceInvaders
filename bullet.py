import pygame


class playerProjectiles:
    def __init__(self, x):
        self.entity = pygame.image.load("player_bullet.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(x.rect.left+25, x.rect.top-50)
        self.entity = pygame.transform.scale(self.entity, (60,26))
        self.entity = pygame.transform.rotate(self.entity, 90)
       
  
class playerProjecticleList:
    def __init__(self, player):
        self.playerProjectileArray = []
        self.player = player
    def createBullet(self):
        print ("ok")
        self.playerProjectileArray.append(playerProjectiles(self.player))
    def moveAll(self):
        bullet = 0
        for bullet in self.playerProjectileArray:
            bullet.rect = bullet.rect.move(0, -6)
