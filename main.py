import math, random, sys, time, pygame, bullet, enemy, enemyBullets, player

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Avoiding Game!')
background = pygame.image.load("background.jpg")
player = player.player(size)
playerBullets = bullet.playerProjecticleList(player)
enemyBullet = enemyBullets.enemyProjecticleList()
enemies = enemy.enemyList(10)
clock = pygame.time.Clock()
currentTime = time.time()
enemies.createEnemy()

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
            if event.key == pygame.K_SPACE:
                playerBullets.createBullet()      
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moveLeft = 0
            if event.key == pygame.K_RIGHT:
                player.moveRight = 0
    if(player.moveRight == 1):
        player.move(5)
    if(player.moveLeft == 1):
        player.move(-5)
    
    x = 0
    for x in enemies.enemyArray:
        enemyBullet.createBullet(x)
    
    enemies.moveAll(playerBullets.playerProjectileArray)
    playerBullets.moveAll()
    enemyBullet.moveAll()
    # TO REMOVE THE OLD IMAGE OF THE MOVED ENEMIES/PLAYER
    screen.blit(background, background.get_rect())
    # DRAWS ALL BULLETS
    x = 0
    for x in playerBullets.playerProjectileArray:
        screen.blit(x.entity, x.rect)
    x = 0
    for x in enemyBullet.enemyProjectileArray:
        screen.blit(x.entity, x.rect)
    # DRAWS ALL ENEMIES
    x = 0
    for x in enemies.enemyArray:
        screen.blit(x.entity, x.rect)
    # DRAWS PLAYER
    screen.blit(player.entity, player.rect)
    # REFRESHES EVERYTHING
    pygame.display.flip()
    clock.tick(120)

