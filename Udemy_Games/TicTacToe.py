import pygame
pygame.init()

sw = 300
sh = 300
offset = sw//20
run2 = True

class player:
    def __init__(self, sym):
        self.sym = sym

    def xdraw(self, x1, y1, x2, y2):
        pygame.draw.line(win, (0, 0, 0), (x1+offset, y1+offset), (x2-offset, y2-offset), 3)
        pygame.draw.line(win, (0, 0, 0), (x1 + sw//3 - offset, y1 + offset), (x2 - sh//3 + offset, y2 - offset), 3)

    def odraw(self, x1, y1, x2, y2):
        pygame.draw.circle(win, (0, 0, 0), ((x1+x2)//2,(y1+y2)//2), (x2-x1)//2-offset+5, 3)

    def draw(self, x1, y1, x2, y2):
        if self.sym == 'X':
            self.xdraw(x1, y1, x2, y2)
        else:
            self.odraw(x1, y1, x2, y2)

    def check(self, A):
        h1 = A[0][0] == self.sym and A[1][0] == self.sym and A[2][0] == self.sym
        h2 = A[0][1] == self.sym and A[1][1] == self.sym and A[2][1] == self.sym
        h3 = A[0][2] == self.sym and A[1][2] == self.sym and A[2][2] == self.sym
        v1 = A[0][0] == self.sym and A[1][0] == self.sym and A[2][0] == self.sym
        v2 = A[0][1] == self.sym and A[1][1] == self.sym and A[2][1] == self.sym
        v3 = A[0][2] == self.sym and A[1][2] == self.sym and A[2][2] == self.sym
        d1 = A[0][0] == self.sym and A[1][1] == self.sym and A[2][2] == self.sym
        d2 = A[0][2] == self.sym and A[1][1] == self.sym and A[2][0] == self.sym

        return h1 or h2 or h3 or v1 or v2 or v3 or d1 or d2

def playagain():
    return input("\nDo You Want To Play Again?(y/n): ").lower() == 'y'

def play(win):
    win.fill((200, 200, 200))
    pygame.display.set_caption("TicTacToe")
    pygame.draw.line(win, (0, 0, 0), (sw // 3, 0), (sw // 3, sh), 3)
    pygame.draw.line(win, (0, 0, 0), ((2 * sw) // 3, 0), ((2 * sw) // 3, sh), 3)
    pygame.draw.line(win, (0, 0, 0), (0, sh // 3), (sw, sh // 3), 3)
    pygame.draw.line(win, (0, 0, 0), (0, (2 * sh) // 3), (sw, (2 * sh) // 3), 3)

while run2:
    p1_Turn = True
    p2_Turn = False
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    A = [['', '', ''], ['', '', ''], ['', '', '']]

    while True:
        ch = input("\nPlayer_1!! Do you want to play as 'X' or 'O': ")
        if ch=='X' or ch=='x':
            p1 = player('X')
            p2 = player('O')
            print("Player_2!! You will play as 'O'")
            break
        elif ch=='O' or ch=='o':
            p1 = player('O')
            p2 = player('X')
            print("Player_2!! You will play as 'X'")
            break
        else:
            print("Wrong Choice!!!\nPlease Try Again\n")

    pygame.time.delay(2000)

    win = pygame.display.set_mode((sw, sh))
    play(win)

    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run2 = False

        keys = pygame.key.get_pressed()

        # When Key 9 is Pressed
        if keys[pygame.K_9] and a[8] == 1:
            if p1_Turn:
                p1.draw((2 * sw) // 3, 0, sw, sh // 3)
                p1_Turn = False
                p2_Turn = True
                A[0][2] = p1.sym
            else:
                p2.draw((2 * sw) // 3, 0, sw, sh // 3)
                p1_Turn = True
                p2_Turn = False
                A[0][2] = p2.sym
            a[8] = 0

        # When Key 8 is pressed
        if keys[pygame.K_8] and a[7] == 1:
            if p1_Turn:
                p1.draw(sw // 3, 0, (2 * sw) // 3, sh // 3)
                p1_Turn = False
                p2_Turn = True
                A[0][1] = p1.sym
            else:
                p2.draw(sw // 3, 0, (2 * sw) // 3, sh // 3)
                p1_Turn = True
                p2_Turn = False
                A[0][1] = p2.sym
            a[7] = 0

        # When Key 7 is pressed
        if keys[pygame.K_7] and a[6] == 1:
            if p1_Turn:
                p1.draw(0, 0, sw // 3, sh // 3)
                p1_Turn = False
                p2_Turn = True
                A[0][0] = p1.sym
            else:
                p2.draw(0, 0, sw // 3, sh // 3)
                p1_Turn = True
                p2_Turn = False
                A[0][0] = p2.sym
            a[6] = 0

        # When Key 6 is pressed
        if keys[pygame.K_6] and a[5] == 1:
            if p1_Turn:
                p1.draw((2 * sw) // 3, sh // 3, sw, (2 * sh) // 3)
                p1_Turn = False
                p2_Turn = True
                A[1][2] = p1.sym
            else:
                p2.draw((2 * sw) // 3, sh // 3, sw, (2 * sh) // 3)
                p1_Turn = True
                p2_Turn = False
                A[1][2] = p2.sym
            a[5] = 0

        # When Key 5 is pressed
        if keys[pygame.K_5] and a[4] == 1:
            if p1_Turn:
                p1.draw(sw // 3, sh // 3, (2 * sw) // 3, (2 * sh) // 3)
                p1_Turn = False
                p2_Turn = True
                A[1][1] = p1.sym
            else:
                p2.draw(sw // 3, sh // 3, (2 * sw) // 3, (2 * sh) // 3)
                p1_Turn = True
                p2_Turn = False
                A[1][1] = p2.sym
            a[4] = 0

        # When Key 4 is pressed
        if keys[pygame.K_4] and a[3] == 1:
            if p1_Turn:
                p1.draw(0, sh // 3, sw // 3, (2 * sh) // 3)
                p1_Turn = False
                p2_Turn = True
                A[1][0] = p1.sym
            else:
                p2.draw(0, sh // 3, sw // 3, (2 * sh) // 3)
                p1_Turn = True
                p2_Turn = False
                A[1][0] = p2.sym
            a[3] = 0

        # When Key 3 is pressed
        if keys[pygame.K_3] and a[2] == 1:
            if p1_Turn:
                p1.draw((2 * sw)//3, (2 * sh)//3, sw, sh)
                p1_Turn = False
                p2_Turn = True
                A[2][2] = p1.sym
            else:
                p2.draw((2 * sw)//3, (2 * sh)//3, sw, sh)
                p1_Turn = True
                p2_Turn = False
                A[2][2] = p2.sym
            a[2] = 0

        # When Key 2 is pressed
        if keys[pygame.K_2] and a[1] == 1:
            if p1_Turn:
                p1.draw(sw // 3, (2 * sh) // 3, (2 * sw) // 3, sh)
                p1_Turn = False
                p2_Turn = True
                A[2][1] = p1.sym
            else:
                p2.draw(sw // 3, (2 * sh) // 3, (2 * sw) // 3, sh)
                p1_Turn = True
                p2_Turn = False
                A[2][1] = p2.sym
            a[1] = 0

        # When Key 1 is pressed
        if keys[pygame.K_1] and a[0] == 1:
            if p1_Turn:
                p1.draw(0, (2 * sh) // 3, sw // 3, sh)
                p1_Turn = False
                p2_Turn = True
                A[2][0] = p1.sym
            else:
                p2.draw(0, (2 * sh) // 3, sw // 3, sh)
                p1_Turn = True
                p2_Turn = False
                A[2][0] = p2.sym
            a[0] = 0

        pygame.display.update()

        if p1.check(A) or p2.check(A):
            pygame.quit()
            if p1.check(A):
                print('\nPlayer_1 Won The Game!!!')
            if p2.check(A):
                print('\nPlayer_2 Won The Game!!!')
            run2 = playagain()
            run = False

        if [0, 0, 0, 0, 0, 0, 0, 0, 0] == a:
            pygame.quit()
            print('\nThe Game Ended in a Draw!!!')
            run2 = playagain()
            run = False

    pygame.quit()



