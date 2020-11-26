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

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self,win):
        if  self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()

man = player(50, 400, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x <= (screenWidth - man.width - man.vel):
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if not man.isJump:
        '''if keys[pygame.K_UP] and man.y >= man.vel:
              man.y -= man.vel
        if keys[pygame.K_DOWN] and man.y <= (screenWidth - man.height - man.vel):
              man.y += man.vel'''

        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()

