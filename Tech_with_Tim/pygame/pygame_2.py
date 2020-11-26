import pygame
pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 8

run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
          x -= vel
    if keys[pygame.K_RIGHT] and x <= (screenWidth - width - vel):
          x += vel

    if not isJump:
        if keys[pygame.K_UP] and y >= vel:
              y -= vel
        if keys[pygame.K_DOWN] and y <= (screenWidth - height - vel):
              y += vel
        if keys[pygame.K_SPACE]:
              isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount<0:
                neg = -1
            y -= (jumpCount ** 2) * 0.25 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0,  0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

