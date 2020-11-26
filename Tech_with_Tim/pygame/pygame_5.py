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
        self.standing = True

    def draw(self,win):
        if  self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

man = player(50, 400, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.right:
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width/2), round(man.y + man.height/2), 3, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x <= (screenWidth - man.width - man.vel):
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
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

