import pygame
import time
import random

pygame.init()

sw = 500
diff = 2
win = pygame.display.set_mode((sw, sw))
pygame.display.set_caption("Snake Game")


class Box:

    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], diff * 8, diff * 8))


class Snake:

    body = []

    def __init__(self, pos, color):
        self.color = color
        self.head = Box(pos, color)
        self.body.append(self.head)
        self.vx = 1
        self.vy = 0

    def add_box(self):
        pos = (self.body[-1].pos[0], self.body[-1].pos[1])
        self.body.append(Box(pos, (0, 255, 0)))

    def update(self):
        prev_positions = []
        for i in range(0, len(self.body)-1):
            prev_positions.append(self.body[i].pos)

        self.body[0].pos = (self.body[0].pos[0] + diff*4*self.vx, self.body[0].pos[1] + diff*4*self.vy)
        for i in range(1, len(self.body)):
            self.body[i].pos = prev_positions[i-1]

    def draw(self):
        for box in self.body:
            box.draw()


class food:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def update(self):
        self.pos = (random.randint(0, 242)*2, random.randint(0, 242)*2)

    def draw(self):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], diff * 8, diff * 8))


# Our Score to be displayed
Score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def display_window():
    win.fill((200, 200, 200))

    score = font.render("Score: " + str(Score_value), True, (255, 255, 255))
    win.blit(score, (textX, textY))


s = Snake((200, 250), (255, 0, 255))
food_pos = (random.randint(0, 242)*2, random.randint(0, 242)*2)
f = food(food_pos, (255, 0, 0))

run = True
while run:
    time.sleep(0.035)
    display_window()
    s.draw()
    s.update()
    f.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                s.vy = -1
                s.vx = 0
            if event.key == pygame.K_DOWN:
                s.vy = 1
                s.vx = 0
            if event.key == pygame.K_LEFT:
                s.vy = 0
                s.vx = -1
            if event.key == pygame.K_RIGHT:
                s.vy = 0
                s.vx = 1

    if s.body[0].pos[0] >= sw - diff*8 and s.vx == 1:
        s.body[0].pos = (-diff*7, s.body[0].pos[1])
    elif s.body[0].pos[0] <= 0 and s.vx == -1:
        s.body[0].pos = (sw - diff, s.body[0].pos[1])
    elif s.body[0].pos[1] <= 0 and s.vy == -1:
        s.body[0].pos = (s.body[0].pos[0], sw - diff)
    elif s.body[0].pos[1] >= sw - diff*8 and s.vy == 1:
        s.body[0].pos = (s.body[0].pos[0], -diff*7)

    if abs(s.body[0].pos[0] - f.pos[0]) < diff * 7.5 and abs(s.body[0].pos[1] - f.pos[1]) < diff * 7.5:
        Score_value += 2
        f.update()
        s.add_box()

    pygame.display.update()

pygame.quit()
