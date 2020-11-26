import pygame
from pygame import mixer
import math
import random

pygame.init()

# loading images
icon = pygame.image.load("icon.png")
playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
bulletImg = pygame.image.load("bullet.png")
explosionImg = pygame.image.load("explosion.png")
backgroundImg = pygame.image.load("background.png")

# loading music and sounds
mixer.music.load("background.wav")
mixer.music.play(-1)  # playing background music in loop
explosionSound = mixer.Sound("explosion.wav")
bulletSound = mixer.Sound("laser.wav")

pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)

sw = 800
sh = 600

initialPlayerX = 368
initialPlayerY = 510
PlayerMovementSpeed = 2.8

BulletMovementSpeed = 1.5

win = pygame.display.set_mode((sw, sh))


class player():

    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx

    def update(self, dir):
        self.x += dir * self.vx

    def draw(self):
        win.blit(playerImg, (self.x, self.y))


class enemy():

    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.dir = 1

    def reset(self):
        self.x = random.randint(1, 735)
        self.y = random.randint(30, 150)
        self.vx = random.randint(1, 4)

    def update(self):
        if self.x > 735 or self.x < 1:
            self.dir = self.dir * (-1)
            self.y += random.randint(20, 30)
        self.x += self.dir * self.vx

    def draw(self):
        win.blit(enemyImg, (self.x, self.y))


class bullet():

    def __init__(self, x, y, vy):
        self.x = x + 16
        self.y = y
        self.vy = vy

    def update(self):
        if self.y >= 0:
            self.y -= self.vy

    def draw(self):
        win.blit(bulletImg, (self.x, self.y))


# used to check for collision with the enemy
def isCollision(x1, x2, y1, y2):
    distance = math.hypot(x1 + 32 - x2 - 16, y1 + 32 - y2 - 16)
    return distance < 28


# Our Score to be displayed
Score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over Text
game_over_bool = False
over_font = pygame.font.Font("freesansbold.ttf", 80)
overX = 170
overY = 250


def display_score(x, y):
    score = font.render("Score: " + str(Score_value), True, (255, 255, 255))
    win.blit(score, (x, y))


def game_over(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    win.blit(over_text, (x, y))


Player = player(initialPlayerX, initialPlayerY, PlayerMovementSpeed)

num_of_enemies = 5
Enemies = []
for i in range(num_of_enemies):
    initialEnemyX = random.randint(1, 735)
    initialEnemyY = random.randint(30, 150)
    EnemyMovementSpeed = random.randint(1, 4)
    Enemies.append(enemy(initialEnemyX, initialEnemyY, EnemyMovementSpeed))

Bullets = []

run = True
while run:
    win.fill((0, 0, 0))
    win.blit(backgroundImg, (0, 0))
    display_score(textX, textY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Firing Bullet when pressed Space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(Bullets) < 4:  # Makes sure that we don't spam bullets
                    Bullets.append(bullet(Player.x, Player.y, BulletMovementSpeed))

    keys = pygame.key.get_pressed()

    # Movements for our Player
    if keys[pygame.K_LEFT]:
        if Player.x > 0:
            Player.update(-1)  # Updates the Player Position with -ve direction
    if keys[pygame.K_RIGHT]:
        if Player.x < sw - 64:
            Player.update(1)  # Updates the Player Position with +ve direction

    for Enemy in Enemies:
        Enemy.update()  # Updating the Enemy Position
        Enemy.draw()  # Drawing the updated Enemy

        if Enemy.y > 200:
            game_over_bool = True
            Enemies = []
            break

        for Bullet in Bullets:
            if Bullet.y == Player.y:
                bulletSound.play()

            Bullet.update()  # Updates position of bullet
            Bullet.draw()  # draws the updated bullet

            # if bullet collides with the enemy
            if isCollision(Enemy.x, Bullet.x, Enemy.y, Bullet.y):
                explosionSound.play()
                win.blit(explosionImg, (Enemy.x, Enemy.y))
                Bullets.pop(Bullets.index(Bullet))
                pygame.time.delay(30)
                Enemy.reset()  # resets the enemy
                Score_value += 1

            # if bullet goes out of screen
            if Bullet.y < 0:
                Bullets.pop(Bullets.index(Bullet))

    Player.draw()  # Drawing the Player

    if game_over_bool:
        game_over(overX, overY)

    pygame.display.update()

pygame.quit()
