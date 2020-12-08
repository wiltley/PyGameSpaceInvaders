import sys, pygame, random

class enemy: 
    def __init__(self, posX, posY):
        self.entity = pygame.image.load("enemy.png").convert_alpha()
        self.entity = pygame.transform.scale(self.entity, (102,72))
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(posX, posY)
        self.speed = [0, random.randint(2,3)]
        self.mask = pygame.mask.from_surface(self.entity)

class enemyList:
    def __init__(self,wave):
        self.wave = wave
        self.enemyArray = []
        self.moveDir = 5
    def createEnemy(self):
        x = 0
        for x in range(0, self.wave):
            self.enemyArray.append(enemy(x*100, 200))

    def moveAll(self, bulletArray):
        x = 0
        for x in self.enemyArray:
            x.rect = x.rect.move(self.moveDir, 0)
            if(x.rect.right >= 1920):
                self.moveDir = -5
            if(x.rect.left <= 0):
                self.moveDir = 5
            
            y = 0
            for y in bulletArray:
                offset_x = x.rect.right - y.rect.right
                offset_y = y.rect.bottom - y.rect.top
                if(x.mask.overlap(y.mask, (offset_x, offset_y))):
                    self.enemyArray.remove(x)
                    bulletArray.remove(y)
