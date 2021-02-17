import pygame
import time
import random

pygame.init()

sw = 500
diff = 2                 # 1 Grid unit size
box_size = 8             # No. of Grid Units
win = pygame.display.set_mode((sw, sw))
pygame.display.set_caption("Snake Game")


class Box:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], diff * box_size, diff * box_size))


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
        for index in range(0, len(self.body)-1):
            prev_positions.append(self.body[index].pos)

        self.body[0].pos = (self.body[0].pos[0] + diff*4*self.vx, self.body[0].pos[1] + diff*4*self.vy)
        for index in range(1, len(self.body)):
            self.body[index].pos = prev_positions[index-1]

    def draw(self):
        for box in self.body:
            box.draw()


class food:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def update(self):
        self.pos = (random.randint(0, sw//2-box_size)*2, random.randint(0, sw//2-box_size)*2)

    def draw(self):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], diff * box_size, diff * box_size))


# Our Score to be displayed
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


# Display Window for Our Game
def display_window():
    # Background of our Game
    win.fill((173, 216, 246))

    # Score Value displayed
    score = font.render("Score: " + str(score_value), True, (50, 50, 50))
    win.blit(score, (textX, textY))

    # Snake drawn and updated / Food is drawn
    s.draw()
    s.update()
    f.draw()


# Initialising Our Snake Head
s = Snake((200, 250), (255, 0, 255))
# Food Position which is randomly selected
food_pos = (random.randint(0, sw//2-box_size)*2, random.randint(0, sw//2-box_size)*2)
# Initialising Our Food
f = food(food_pos, (255, 0, 0))

run = True
while run:
    time.sleep(0.035)
    display_window()

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

    # Snake Teleporting When Going Outside Boundary
    if s.body[0].pos[0] >= sw - diff*8 and s.vx == 1:
        s.body[0].pos = (-diff*7, s.body[0].pos[1])
    elif s.body[0].pos[0] <= 0 and s.vx == -1:
        s.body[0].pos = (sw - diff, s.body[0].pos[1])
    elif s.body[0].pos[1] <= 0 and s.vy == -1:
        s.body[0].pos = (s.body[0].pos[0], sw - diff)
    elif s.body[0].pos[1] >= sw - diff*8 and s.vy == 1:
        s.body[0].pos = (s.body[0].pos[0], -diff*7)

    # Snake Cut its Tail
    for i in range(1, len(s.body) - 1):
        if s.body[0].pos == s.body[i].pos:
            del s.body[i:]
            # Decrementing Score Value
            score_value -= 20
            break

    # Snake Eats The Food
    if abs(s.body[0].pos[0] - f.pos[0]) < diff * (box_size-0.5) and \
            abs(s.body[0].pos[1] - f.pos[1]) < diff * (box_size-0.5):
        # Incrementing Score Value
        score_value += 4
        f.update()
        s.add_box()

    pygame.display.update()

pygame.quit()
