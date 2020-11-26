import pygame
pygame.init()

screenWidth = 500
screenHeight = 480
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R1.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R2.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R3.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R4.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R5.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R6.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R7.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R8.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\R9.png')]
walkLeft = [pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L1.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L2.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L3.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L4.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L5.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L6.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L7.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L8.png'), pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\L9.png')]
bg = pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\bg.jpg')
char = pygame.image.load(r'C:\Users\M K DE\PycharmProjects\tensorEnv\Tech with Tim- pygame\pygame_images\standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x <= (screenWidth - width - vel):
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        '''if keys[pygame.K_UP] and y >= vel:
              y -= vel
        if keys[pygame.K_DOWN] and y <= (screenWidth - height - vel):
              y += vel'''

        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.25 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()

