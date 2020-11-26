import pygame
import pickle
#import pandas as pd
#from sklearn.neighbors import KNeighborsRegressor

'''pong = pd.read_csv("PongGame.csv")
pong = pong.drop_duplicates()

X = pong.drop(columns="Paddle.y")
y = pong["Paddle.y"]

clf = KNeighborsRegressor(n_neighbors=3)
clf = clf.fit(X, y)
pickle.dump(clf, open("PongGame_model.pickle", 'wb'))'''

clf = pickle.load(open("PongGame_model.pickle", 'rb'))
#df = pd.DataFrame(columns=['x', 'y', 'vx', 'vy'])

pygame.init()

sw = 800
sh = 450
border = sh//30
vx = -2
vy = -2
pw = sw*0.02
ph = sh*0.24
border_color = (235, 235, 235)
offset = 1

class Ball():

    fgcolor = (200, 200, 200)
    bgcolor = (0, 0, 0)
    radius = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, win, d=1):
        if d==1:
             pygame.draw.circle(win, Ball.fgcolor, (self.x, self.y), Ball.radius)
        else:
             pygame.draw.circle(win, Ball.bgcolor, (self.x, self.y), Ball.radius)

    def update(self, win):
        self.show(win, 0)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(win)

    def bcheck(self):
        if self.y < border + Ball.radius + offset or self.y > sh - border - Ball.radius - offset:
            self.vy *= -1
        if self.x < border + Ball.radius + offset:
            self.vx *= -1

    def pcheck(self, paddle):
        if self.x > sw - Ball.radius - border - offset and self.y < paddle.y + paddle.height and self.y > paddle.y:
            self.vx *= -1

class Paddle():

    fgcolor = (200, 200, 200)
    bgcolor = (0, 0, 0)

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self, win, d=1):
        if d==1:
            pygame.draw.rect(win, Paddle.fgcolor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(win, Paddle.bgcolor, (self.x, self.y, self.width, self.height))

    def update(self, win):
        p = pygame.mouse.get_pos()[1]
        if p > border and p < sh - border - ph:
            self.show(win, 0)
            self.y = p
            self.show(win)

    def updateAI(self, win, p):
        if p > border and p < sh - border - ph:
            self.show(win, 0)
            self.y = p
            self.show(win)

#sample = open("PongGame.csv","w")
#print("x,y,vx,vy,Paddle.y", file=sample)

Run = True
while Run:

    win = pygame.display.set_mode((sw, sh))
    pygame.draw.rect(win, border_color, (0, 0, sw, border))
    pygame.draw.rect(win, border_color, (0, 0, border, sh))
    pygame.draw.rect(win, border_color, (0, sh-border, sw, border))

    pygame.mouse.set_pos([sw - pw, sh//2-ph//2])
    pygame.mouse.set_visible(False)
    ball = Ball(sw-border-Ball.radius, sh//2, vx, vy)
    paddle = Paddle(sw-pw, sh//2-ph//2, pw, ph)
    paddle.show(win)

    run = True
    while run:
        pygame.time.delay(4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                Run = False

        ball.show(win)

        #paddle.update(win)
        ball.update(win)
        ball.bcheck()
        ball.pcheck(paddle)

        #toPredict = df.append({'x': ball.x, 'y':ball.y, 'vx': ball.vx, 'vy': ball.vy}, ignore_index=True)
        toPredict = [[ball.x, ball.y, ball.vx, ball.vy]]
        PaddlePos = clf.predict(toPredict)

        paddle.updateAI(win, PaddlePos)
        #print("{},{},{},{},{}".format(ball.x, ball.y, ball.vx, ball.vy, paddle.y), file=sample)

        if ball.x > sw - ball.radius + offset:
            run = False

        pygame.display.flip()

pygame.quit()