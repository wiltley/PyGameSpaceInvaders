import pygame

class playerProjectiles(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.entity = pygame.image.load("../assets/playerbullet.png").convert_alpha()
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(x.rect.left+29, x.rect.top-50)
        self.entity = pygame.transform.scale(self.entity, (45,19))
        self.entity = pygame.transform.rotate(self.entity, 90)
        self.mask = pygame.mask.from_surface(self.entity)
        self.playershot = pygame.mixer.music.load('../assets/playershot.mp3')
        self.playershot = pygame.mixer.music.play(0)
    def checkBounds(self):
        if self.rect.top <= 0:
            return 1
class playerProjecticleList:
    def __init__(self, player):
        self.playerProjectileArray = []
        self.player = player
    def createBullet(self):
        self.playerProjectileArray.append(playerProjectiles(self.player))
    def moveAll(self):
        bullet = 0
        for bullet in self.playerProjectileArray:
            bullet.rect = bullet.rect.move(0, -15)
            
            if bullet.checkBounds() == 1:
                self.playerProjectileArray.remove(bullet)