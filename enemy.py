import sys, pygame, random

class enemy(pygame.sprite.Sprite): 
    def __init__(self, posX, posY):
        super().__init__()
        self.entity = pygame.image.load("enemy.png").convert_alpha()
        self.entity = pygame.transform.scale(self.entity, (102,72))
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(posX, posY)
        self.speed = [0, random.randint(2,3)]
        self.mask = pygame.mask.from_surface(self.entity)
        self.moveDirection = 5
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
            x.rect = x.rect.move(x.moveDirection, 0)
            if(x.rect.right >= 1920):
                x.moveDirection = -5
            if(x.rect.left <= 0):
                x.moveDirection = 5
            y = 0
            for y in bulletArray:
                offset_x = x.rect.right - y.rect.left
                offset_y = y.rect.bottom - x.rect.bottom
                if(x.mask.overlap_area(y.mask, (offset_x, offset_y))):
                    self.enemyArray.remove(x)
                    bulletArray.remove(y)
