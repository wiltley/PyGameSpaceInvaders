import sys, pygame, random

class enemy: 
    def __init__(self, size):
        self.entity = pygame.image.load("ufo.png")
        self.rect = self.entity.get_rect()
        self.rect = self.rect.move(random.randint(0,265), random.randint(-800,0))
        self.speed = [0, random.randint(2,3)]
        self.size = size
    def moveDown(self):
        self.rect = self.rect.move(self.speed)
    def destroy(self):
        if self.rect.bottom == (self.size[1]):
            return 1
    def checkCollision(self, player):
        if(self.rect.bottom <= player.rect.top+15 and self.rect.bottom>= player.rect.top):
            return self.rect.colliderect(player.rect)