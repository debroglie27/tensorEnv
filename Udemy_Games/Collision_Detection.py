import pygame
import time
import math

pygame.init()

sw = 500
win = pygame.display.set_mode((sw, sw))
pygame.display.set_caption("Collision Detection")
acceleration = 500


class Ball:
    def __init__(self, radius, colour, pos=(250, 250), vel=(-50, 0), mass=2):
        self.radius = radius
        self.colour = colour
        self.posX = pos[0]
        self.posY = pos[1]
        self.vX = vel[0]
        self.vY = vel[1]
        self.mass = mass
        self.acc = acceleration

    def detect_boundary_collision(self):
        if self.posX < self.radius or self.posX > sw - self.radius:
            self.vX *= -1
            if self.posX < self.radius:
                self.posX += 2
            else:
                self.posX -= 2
        if self.posY > sw - self.radius:
            self.vY *= -1

    def update(self, dt):
        self.detect_boundary_collision()
        prev_vY = self.vY
        self.vY = self.vY + self.acc*dt
        self.posX = self.posX + self.vX * dt
        self.posY = self.posY + prev_vY * dt + 0.5 * self.acc * dt * dt

    def draw(self):
        pygame.draw.circle(win, self.colour, (int(self.posX), int(self.posY)), self.radius)


def detect_ball_collision():
    dist_between_balls = math.hypot(ball1.posY - ball2.posY, ball1.posX - ball2.posX)
    if dist_between_balls <= ball1.radius + ball2.radius:
        cos_theta = (ball1.posX - ball2.posX)/dist_between_balls
        sin_theta = (ball1.posY - ball2.posY)/dist_between_balls

        ball1_velocity_component = ((ball1.mass-ball2.mass)/(ball1.mass+ball2.mass))*(ball1.vX*cos_theta + ball1.vY*sin_theta) + ((2*ball2.mass)/(ball1.mass + ball2.mass))*(ball2.vX*cos_theta + ball2.vY*sin_theta)
        ball1.vX = ball1_velocity_component*cos_theta + ball1.vX*sin_theta*sin_theta + ball1.vY*cos_theta*sin_theta
        ball1.vY = ball1_velocity_component*sin_theta + ball1.vY*cos_theta*cos_theta + ball1.vX*cos_theta*sin_theta

        ball2_velocity_component = ((2*ball1.mass)/(ball1.mass+ball2.mass))*(ball1.vX*cos_theta + ball1.vY*sin_theta) - ((ball1.mass-ball2.mass)/(ball1.mass + ball2.mass))*(ball2.vX*cos_theta + ball2.vY*sin_theta)
        ball2.vX = ball2_velocity_component*cos_theta + ball2.vX*sin_theta*sin_theta + ball2.vY*cos_theta*sin_theta
        ball2.vY = ball2_velocity_component*sin_theta + ball2.vY*cos_theta*cos_theta + ball2.vX*cos_theta*sin_theta


def display_window(dt):
    win.fill((255, 255, 255))

    ball1.draw()
    ball2.draw()
    ball1.update(dt)
    ball2.update(dt)

    pygame.display.update()


ball1 = Ball(20, (255, 0, 0), (250, 220), (-40, 0), 1)
ball2 = Ball(40, (0, 255, 0), (250, 300), (50, 0), 8)
run = True
while run:
    time.sleep(1/100)
    detect_ball_collision()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display_window(1 / 60)

pygame.quit()
