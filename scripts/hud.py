import pygame

class hud:
    def __init__(self):
        self.health = pygame.image.load("../assets/healthfull.png").convert_alpha()
        self.health = pygame.transform.scale(self.health, (315,36))
        self.healthrect = self.health.get_rect()
    
        self.healthArray = []
        self.startMessage = pygame.image.load("../assets/begin.png").convert_alpha()
        self.startMessageRect = self.startMessage.get_rect()
        self.startMessageRect = self.startMessageRect.move(100,400)

        self.score = pygame.image.load("../assets/Score_.png").convert_alpha()
        self.score = pygame.transform.scale(self.score, (170,63))
        self.scoreRect = self.score.get_rect()
        self.scoreRect = self.scoreRect.move(800, 10)

        self.highscore = pygame.image.load("../assets/High score_.png").convert_alpha()
        self.highscore = pygame.transform.scale(self.highscore, (231,70))
        self.highscoreRect = self.score.get_rect()
        self.highscoreRect = self.highscoreRect.move(400, 0)

        self.font = pygame.font.Font('freesansbold.ttf', 25)
        self.scoreFont = 0
        self.highscoreFont = 0
        self.scoreFontRect = 0
        self.highscoreFont = 0
        self.highscoreFontRect = 0
        

    def updateHud(self, player):
        lives = player
        self.scoreFont = self.font.render(str(lives.score), 0, (255,255,255))
        self.highscoreFont = self.font.render(str(lives.highscore), 0, (255,255,255))
        lives = lives.lives
        self.scoreFontRect = self.scoreFont.get_rect()
        self.highscoreFontRect = self.highscoreFont.get_rect()
        self.highscoreFontRect = self.highscoreFontRect.move(650,30)
        self.scoreFontRect = self.scoreFontRect.move(1000,30)

        if lives == 3: 
            self.health = pygame.image.load("../assets/healthfull.png").convert_alpha()
            self.health = pygame.transform.scale(self.health, (315,36))
            self.healthrect = self.health.get_rect()
            self.healthrect = self.healthrect.move(0,15)
        if lives == 2: 
            self.health = pygame.image.load("../assets/health2.png").convert_alpha()
            self.health = pygame.transform.scale(self.health, (315,36))
            self.healthrect = self.health.get_rect()
            self.healthrect = self.healthrect.move(0,15)
        if lives == 1: 
            self.health = pygame.image.load("../assets/health1.png").convert_alpha()
            self.health = pygame.transform.scale(self.health, (315,36))
            self.healthrect = self.health.get_rect()
            self.healthrect = self.healthrect.move(0,15)
        if lives == 0: 
            self.health = pygame.image.load("../assets/ur dead x_X.png").convert_alpha()
            self.health = pygame.transform.scale(self.health, (231,63))
            self.healthrect = self.health.get_rect()
            self.healthrect = self.healthrect.move(0,0)