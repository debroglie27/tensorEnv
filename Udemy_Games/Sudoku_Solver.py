import pygame

pygame.init()

sw = 360
sh = 360
icon = pygame.image.load("sudoku_icon.png")

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

win = pygame.display.set_mode((sw, sh))
pygame.display.set_icon(icon)
pygame.display.set_caption("Sudoku Solver")

number_font = pygame.font.Font("freesansbold.ttf", 30)


def show_num(x, y, n):
    number_text = number_font.render(f"{n}", True, (0, 0, 0))
    win.blit(number_text, (x+12, y+8))


def display_sudoku():
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, sw, sh), 3)
    pygame.draw.line(win, (0, 0, 0), (sh // 3, 0), (sh // 3, sh), 3)
    pygame.draw.line(win, (0, 0, 0), (2 * sh // 3, 0), (2 * sh // 3, sh), 3)
    pygame.draw.line(win, (0, 0, 0), (0, sw // 3), (sw, sw // 3), 3)
    pygame.draw.line(win, (0, 0, 0), (0, 2 * sw // 3), (sw, 2 * sw // 3), 3)

    pygame.draw.line(win, (0, 0, 0), (sh // 9, 0), (sh // 9, sh))
    pygame.draw.line(win, (0, 0, 0), (2 * sh // 9, 0), (2 * sh // 9, sh))
    pygame.draw.line(win, (0, 0, 0), (4 * sh // 9, 0), (4 * sh // 9, sh))
    pygame.draw.line(win, (0, 0, 0), (5 * sh // 9, 0), (5 * sh // 9, sh))
    pygame.draw.line(win, (0, 0, 0), (7 * sh // 9, 0), (7 * sh // 9, sh))
    pygame.draw.line(win, (0, 0, 0), (8 * sh // 9, 0), (8 * sh // 9, sh))

    pygame.draw.line(win, (0, 0, 0), (0, sw // 9), (sw, sw // 9))
    pygame.draw.line(win, (0, 0, 0), (0, 2 * sw // 9), (sw, 2 * sw // 9))
    pygame.draw.line(win, (0, 0, 0), (0, 4 * sw // 9), (sw, 4 * sw // 9))
    pygame.draw.line(win, (0, 0, 0), (0, 5 * sw // 9), (sw, 5 * sw // 9))
    pygame.draw.line(win, (0, 0, 0), (0, 7 * sw // 9), (sw, 7 * sw // 9))
    pygame.draw.line(win, (0, 0, 0), (0, 8 * sw // 9), (sw, 8 * sw // 9))


def display_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                continue
            show_num(j*sw//9, i*sh//9, grid[i][j])


def highlight(x1, y1):
    x0 = (x1 // 40) * 40 + 1
    y0 = (y1 // 40) * 40 + 1

    pygame.draw.rect(win, (255, 0, 0), (x0, y0, sw // 9 - 1, sh // 9 - 1))


def print_board(bo):
    print("\n")
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def possible(x, y, n):
    global grid
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[x0 + i][y0 + j] == n:
                return False
    return True


def solve():
    global grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if possible(i, j, n):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return
    print_board(grid)


fixed = False

run = True
while run:
    display_sudoku()

    if not fixed:
        x, y = pygame.mouse.get_pos()

    highlight(x, y)

    display_grid(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                fixed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                solve()
                run = False

    keys = pygame.key.get_pressed()

    if fixed:
        if keys[pygame.K_1]:
            grid[y//40][x//40] = 1
            fixed = False
        if keys[pygame.K_2]:
            grid[y//40][x//40] = 2
            fixed = False
        if keys[pygame.K_3]:
            grid[y//40][x//40] = 3
            fixed = False
        if keys[pygame.K_4]:
            grid[y//40][x//40] = 4
            fixed = False
        if keys[pygame.K_5]:
            grid[y//40][x//40] = 5
            fixed = False
        if keys[pygame.K_6]:
            grid[y//40][x//40] = 6
            fixed = False
        if keys[pygame.K_7]:
            grid[y//40][x//40] = 7
            fixed = False
        if keys[pygame.K_8]:
            grid[y//40][x//40] = 8
            fixed = False
        if keys[pygame.K_9]:
            grid[y//40][x//40] = 9
            fixed = False
        if keys[pygame.K_BACKSPACE]:
            grid[y//40][x//40] = 0
            fixed = False

    pygame.display.update()

pygame.quit()
