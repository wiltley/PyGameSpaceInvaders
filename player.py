import sys, pygame

class player(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.entity = pygame.image.load("player.png").convert_alpha()
        self.entity = pygame.transform.scale(self.entity, (92,106))
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(800,870)
        self.mask = pygame.mask.from_surface(self.entity)
        self.speed = [1, 0]
        self.moveRight = 0
        self.moveLeft = 0
        self.lives = 5
    def move(self, dir):
        if(self.rect.left == 0):
            self.rect = self.rect.move(5,0)
        elif(self.rect.right == 300):
            self.rect = self.rect.move(-10,0)
        else:
            self.rect = self.rect.move(dir,0)
    def gotHit(self):
        self.lives-=1