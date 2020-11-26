import pygame

pygame.init()

sw = 500
diff = 20
win = pygame.display.set_mode((sw, sw))
pygame.display.set_caption("Snake Game")


class Box():

    def __init__(self, dirx, diry, pos, color):
        self.pos = pos
        self.color = color
        self.dirx = 1
        self.diry = 0

    def update(self):
        if self.pos[0] == 0 and self.dirx == -1:
            self.pos[0] = sw//diff - 1
        elif self.pos[0] == sw//diff - 1 and self.dirx == 1:
            self.pos[0] = 0
        elif self.pos[1] == 0 and self.diry == -1:
            self.pos[1] = sw//diff - 1
        elif self.pos[1] == sw//diff-1 and self.dirx == 1:
            self.pos[1] = 0
        else:
            self.pos[0] += self.dirx*diff
            self.pos[1] += self.dirx*diff

    def draw(self):
        pygame.draw.rect(win, self.color, (self.pos[0], self.pos[1], diff, diff))


class Snake():

    body = []
    turns = {}

    def __init__(self, pos, color):
        self.color = color
        self.head = Box(pos, color)
        self.body.append(self.head)
        self.dirx = 1
        self.diry = 0

    def add_box(self, pos):
        self.body.append(Box(pos, self.color))

    def add_turn(self, pos, dx, dy):
        self.turns[pos] = (dx, dy)

    def update(self):
        for box in self.body:
            box.update()

    def draw(self):

        for p in self.turns:
            for box in self.body:

                if box.pos == p:
                    box.dirx, box.diry = self.turns[p]
                box.draw()





def display_window():
    win.fill((0, 0, 0))
    x = diff
    y = diff

    for i in range(sw//diff):
        pygame.draw.line(win, (255, 255, 255), (x, 0), (x, sw))
        pygame.draw.line(win, (255, 255, 255), (0, y), (sw, y))
        x += diff
        y += diff


s = Snake((10, 10), (255, 0, 0))

run = True
while run:

    display_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                s.add_turn(s.head.pos, 0, -1)
            if event.key == pygame.K_DOWN:
                s.add_turn(s.head.pos, 0, 1)
            if event.key == pygame.K_LEFT:
                s.add_turn(s.head.pos, -1, 0)
            if event.key == pygame.K_RIGHT:
                s.add_turn(s.head.pos, 1, 0)



    pygame.display.update()

pygame.quit()

