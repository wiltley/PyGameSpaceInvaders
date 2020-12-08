import sys, pygame, random

class enemy(pygame.sprite.Sprite): 
    def __init__(self, posX, posY):
        super().__init__()

        randomEntity = []
        randomEntity = [pygame.image.load("spaceinvader1.png").convert_alpha(), pygame.image.load("spaceinvader2.png").convert_alpha(), pygame.image.load("spaceinvader3.png").convert_alpha()]
        self.entity = randomEntity[random.randint(0,2)]
        self.entity = pygame.transform.scale(self.entity, (87,63))
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
        self.spawnY = 100
    def createEnemy(self):
        x = 0
        y = 100
        for x in range(0, self.wave):
            self.enemyArray.append(enemy(x*100, self.spawnY))
            if len(self.enemyArray)%10 == 0:
                self.spawnY += 100

    def moveAll(self, bulletArray, player):
        x = 0
        for x in self.enemyArray:
            x.rect = x.rect.move(x.moveDirection, 0)
            if(x.rect.right >= 1080):
                x.moveDirection = -5
            if(x.rect.left <= 0):
                x.moveDirection = 5
            y = 0
            for y in bulletArray:
                offset_x = x.rect.right - y.rect.left
                offset_y = y.rect.bottom - x.rect.bottom
                if(x.mask.overlap_area(y.mask, (offset_x, offset_y))):
                    self.enemyArray.remove(x)
                    player.score += 110

                    if player.score >= player.highscore:
                        player.highscore = player.score
                    bulletArray.remove(y)
