import math, random, sys, time, pygame, bullet, enemy, enemyBullets, player, hud

pygame.init()
size = width, height = 1080, 1080
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Avoiding Game!')
background = pygame.image.load("../assets/background.jpg")
player = player.player(size)
playerBullets = bullet.playerProjecticleList(player)
enemyBullet = enemyBullets.enemyProjecticleList()
waveSpawn = 0
enemies = enemy.enemyList()
clock = pygame.time.Clock()
currentTime = time.time()
hud = hud.hud()
gameRunning = 0


while 1:
    # IF QUIT AND MOVEMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moveRight = 1
                player.moveLeft = 0    
            if event.key == pygame.K_LEFT:
                player.moveLeft = 1
                player.moveRight = 0
            if event.key == pygame.K_SPACE and gameRunning == 1:
                playerBullets.createBullet()     
            if event.key == pygame.K_SPACE and gameRunning == 0:
                gameRunning = 1
                player.reset()
                hud.updateHud(player) 
                waveSpawn = 0       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moveLeft = 0
            if event.key == pygame.K_RIGHT:
                player.moveRight = 0
    if(player.moveRight == 1):
        player.move(5)
    if(player.moveLeft == 1):
        player.move(-5)
    

    screen.blit(background, background.get_rect())
    # CREATES NEW ENEMY BULLETS RANDOMLY
    if gameRunning == 1:
        x = 0
        if len(enemies.enemyArray) == 0:
            waveSpawn += 5
            enemies.createEnemy(waveSpawn);
            player.lives = 3
        x = 0
        for x in enemies.enemyArray:
            enemyBullet.createBullet(x)
        # MOVES EVERYONE
        enemies.moveAll(playerBullets.playerProjectileArray, player)
        enemyBullet.moveAll(player)
        # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
        # DRAWS ALL PLAYER BULLETS
        playerBullets.moveAll()
        x = 0
        for x in playerBullets.playerProjectileArray:
            screen.blit(x.entity, x.rect)
        # DRAWS ALL ENEMY BULLETS
        x = 0
        for x in enemyBullet.enemyProjectileArray:
            screen.blit(x.entity, x.rect)
        # DRAWS ALL ENEMIES
        x = 0
        for x in enemies.enemyArray:
            screen.blit(x.entity, x.rect)
        if player.lives <= 0:
            gameRunning = 0

    if gameRunning == 0:
        screen.blit(hud.startMessage,hud.startMessageRect)      
        enemies.enemyArray = []  
        enemyBullet.enemyProjectileArray = []
        playerBullets.playerProjectileArray = []
    # DRAWS PLAYER
    screen.blit(player.entity, player.rect)
    # REFRESHES EVERYTHING
    hud.updateHud(player)
    screen.blit(hud.health, hud.healthrect)
    screen.blit(hud.score, hud.scoreRect)
    screen.blit(hud.highscore, hud.highscoreRect)
    screen.blit(hud.scoreFont, hud.scoreFontRect)
    screen.blit(hud.highscoreFont, hud.highscoreFontRect)

    pygame.display.flip()
    clock.tick(120)