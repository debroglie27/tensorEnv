import pygame
pygame.init()

sw = 500
sh = 600
offset1 = 28
offset2 = 35
offset3 = 64
rad = 20

pygame.display.set_caption("Ludo Game")

def display_board(win):
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (220, 220, 220), (0, (sh-sw)//2, sw, sw))

    # Drawing the Squares
    # Red Square
    pygame.draw.rect(win, (230, 0, 0), (0, (sh-sw)//2 + (6.2*sw)//10, (3.8*sw)//10, (3.8*sw)//10))
    # Green Square
    pygame.draw.rect(win, (0, 230, 0), (0, (sh-sw)//2, (3.8*sw)//10, (3.8*sw)//10))
    # Yellow Square
    pygame.draw.rect(win, (220, 220, 0), ((6.2*sw)//10, (sh-sw)//2, (3.8*sw)//10, (3.8*sw)//10))
    # Blue Square
    pygame.draw.rect(win, (0, 120, 250), ((6.2*sw)//10, (sh-sw)//2 + (6.2*sw)//10, (3.8*sw)//10, (3.8*sw)//10))

    # Drawing the white squares
    pygame.draw.rect(win, (255, 255, 255), (offset1, (sh-sw)//2 + (6.2*sw)//10 + offset1, (3.8*sw)//10 - 2*offset1, (3.8*sw)//10 - 2*offset1))
    pygame.draw.rect(win, (255, 255, 255), (offset1, (sh-sw)//2 + offset1, (3.8*sw)//10 - 2*offset1, (3.8*sw)//10 - 2*offset1))
    pygame.draw.rect(win, (255, 255, 255), ((6.2*sw)//10 + offset1, (sh-sw)//2 + offset1, (3.8*sw)//10 - 2*offset1, (3.8 * sw)//10 - 2*offset1))
    pygame.draw.rect(win, (255, 255, 255), ((6.2*sw)//10 + offset1, (sh-sw)//2 + (6.2*sw)//10 + offset1, (3.8*sw)//10 - 2*offset1, (3.8*sw)//10 - 2*offset1))

    # Drawing the Triangles
    # Red Triangle
    pygame.draw.polygon(win, (230, 0, 0), [((3.8*sw)//10, (sh-sw)//2 + (6.2*sw)//10), (sw//2, sh//2), ((6.2*sw)//10, (sh-sw)//2 + (6.2*sw)//10)])
    # Green Triangle
    pygame.draw.polygon(win, (0, 230, 0), [((3.8*sw)//10, (sh-sw)//2 + (6.2*sw)//10), (sw//2, sh//2), ((3.8*sw)//10, (sh-sw)//2 + (3.8*sw)//10)])
    # Yellow Triangle
    pygame.draw.polygon(win, (220, 220, 0), [((6.2*sw)//10, (sh-sw)//2 + (3.8*sw)//10), (sw//2, sh//2), ((3.8*sw)//10, (sh-sw)//2 + (3.8*sw)//10)])
    # Blue Triangle
    pygame.draw.polygon(win, (0, 120, 250), [((6.2*sw)//10, (sh-sw)//2 + (3.8*sw)//10), (sw//2, sh//2), ((6.2*sw)//10, (sh-sw)//2 + (6.2*sw)//10)])

    # Drawing the circles
    # Red Circles
    pygame.draw.circle(win, (230, 0, 0), (offset1 + offset2, int((sh-sw)//2 + (6.2*sw)//10 + offset1 + offset2)), rad)
    pygame.draw.circle(win, (230, 0, 0), (offset1 + offset2 + offset3, int((sh - sw) // 2 + (6.2 * sw) // 10 + offset1 + offset2)), rad)
    pygame.draw.circle(win, (230, 0, 0), (offset1 + offset2, int((sh - sw) // 2 + (6.2 * sw) // 10 + offset1 + offset2 + offset3)), rad)
    pygame.draw.circle(win, (230, 0, 0), (offset1 + offset2 + offset3, int((sh - sw) // 2 + (6.2 * sw) // 10 + offset1 + offset2 + offset3)), rad)

    # Green Circles
    pygame.draw.circle(win, (0, 230, 0), (offset1 + offset2, (sh-sw)//2 + offset1 + offset2), rad)
    pygame.draw.circle(win, (0, 230, 0), (offset1 + offset2 + offset3, (sh-sw)//2 + offset1 + offset2), rad)
    pygame.draw.circle(win, (0, 230, 0), (offset1 + offset2, (sh-sw)//2 + offset1 + offset2 + offset3), rad)
    pygame.draw.circle(win, (0, 230, 0), (offset1 + offset2 + offset3, (sh-sw)//2 + offset1 + offset2 + offset3), rad)

    # Yellow Circles
    pygame.draw.circle(win, (220, 220, 0), (int((6.2*sw)//10) + offset1 + offset2, (sh-sw)//2 + offset1 + offset2), rad)
    pygame.draw.circle(win, (220, 220, 0), (int((6.2*sw)//10) + offset1 + offset2 + offset3, (sh-sw)//2 + offset1 + offset2), rad)
    pygame.draw.circle(win, (220, 220, 0), (int((6.2*sw)//10) + offset1 + offset2, (sh-sw)//2 + offset1 + offset2 + offset3), rad)
    pygame.draw.circle(win, (220, 220, 0), (int((6.2*sw)//10) + offset1 + offset2 + offset3, (sh-sw)//2 + offset1 + offset2 + offset3), rad)

    # Blue Circles
    pygame.draw.circle(win, (0, 120, 255), (int((6.2 * sw)//10) + offset1 + offset2, (sh-sw)//2 + int((6.2*sw)//10) + offset1 + offset2), rad)
    pygame.draw.circle(win, (0, 120, 255), (int((6.2 * sw)//10) + offset1 + offset2 + offset3, (sh-sw)//2 + int((6.2*sw)//10) + offset1 + offset2), rad)
    pygame.draw.circle(win, (0, 120, 255), (int((6.2 * sw)//10) + offset1 + offset2, (sh-sw)//2 + int((6.2*sw)//10) + offset1 + offset2 + offset3), rad)
    pygame.draw.circle(win, (0, 120, 255), (int((6.2 * sw)//10) + offset1 + offset2 + offset3, (sh-sw)//2 + int((6.2*sw)//10) + offset1 + offset2 + offset3), rad)

    # Drawing the L-shaped Areas
    # Red
    pygame.draw.polygon(win, (230, 0, 0), [((4.6*sw)//10, (sh-sw)//2 + (6.2*sw)//10), ((5.4*sw)//10, (sh-sw)//2 + (6.2*sw)//10), ((5.4*sw)//10, sh - (sh-sw)//2 - (1/6)*(3.8*sw)//10), ((3.8*sw)//10, sh - (sh-sw)//2 - (1/6)*(3.8*sw)//10), ((3.8*sw)//10, sh - (sh-sw)//2 - (1/3)*(3.8*sw)//10), ((4.6*sw)//10, sh - (sh-sw)//2 - (1/3)*(3.8*sw)//10)])
    # Green
    pygame.draw.polygon(win, (0, 230, 0), [((3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2), ((3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2), ((1/6)*(3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2), ((1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((1/3)*(3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2)])
    # Yellow
    pygame.draw.polygon(win, (220, 220, 0), [((5.4*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((4.6*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((4.6*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2), ((5.4*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2)])
    # Blue
    pygame.draw.polygon(win, (0, 120, 250), [((6.2*sw)//10, (5.4*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (4.6*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2)])


def display_lines(win):
    # Big lines
    # Vertical
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (sh-sw)//2), ((3.8*sw)//10, sh - (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10, (sh-sw)//2), ((6.2*sw)//10, sh - (sh-sw)//2))
    # Horizontal
    pygame.draw.line(win, (0, 0, 0), (0, (3.8*sw)//10 + (sh-sw)//2), (sw, (3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), (0, (6.2*sw)//10 + (sh-sw)//2), (sw, (6.2*sw)//10 + (sh-sw)//2))

    # Medium Lines
    # For Yellow
    pygame.draw.line(win, (0, 0, 0), ((4.6*sw)//10, (sh-sw)//2), ((4.6*sw)//10, (3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((5.4*sw)//10, (sh-sw)//2), ((5.4*sw)//10, (3.8*sw)//10 + (sh-sw)//2))
    # For Red
    pygame.draw.line(win, (0, 0, 0), ((4.6*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((4.6*sw)//10, sw + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((5.4*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((5.4*sw)//10, sw + (sh-sw)//2))
    # For Green
    pygame.draw.line(win, (0, 0, 0), (0, (4.6*sw)//10 + (sh-sw)//2), ((3.8*sw)//10, (4.6*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), (0, (5.4*sw)//10 + (sh-sw)//2), ((3.8*sw)//10, (5.4*sw)//10 + (sh-sw)//2))
    # For Blue
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10, (4.6*sw)//10 + (sh-sw)//2), (sw, (4.6*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10, (5.4*sw)//10 + (sh-sw)//2), (sw, (5.4*sw)//10 + (sh-sw)//2))

    # Center Lines
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (3.8*sw)//10 + (sh-sw)//2))

    # Short Lines
    # b/w Red and Green
    pygame.draw.line(win, (0, 0, 0), ((1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((1/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((1/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((1/2)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((1/2)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((2/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((5/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))

    # b/w Yellow and Green
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (1/6)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (1/3)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (1/2)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (1/2)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (2/3)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (2/3)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (5/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (5/6)*(3.8*sw)//10 + (sh-sw)//2))

    # b/w Yellow and Blue
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10 + (1/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (1/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10 + (1/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (1/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10 + (1/2)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (1/2)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (2/3)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10 + (5/6)*(3.8*sw)//10, (6.2*sw)//10 + (sh-sw)//2))

    # b/w Red and Blue
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (1/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (1/6)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (1/3)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (1/3)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (1/2)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (1/2)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (2/3)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (2/3)*(3.8*sw)//10 + (sh-sw)//2))
    pygame.draw.line(win, (0, 0, 0), ((3.8*sw)//10, (6.2*sw)//10 + (5/6)*(3.8*sw)//10 + (sh-sw)//2), ((6.2*sw)//10, (6.2*sw)//10 + (5/6)*(3.8*sw)//10 + (sh-sw)//2))





win = pygame.display.set_mode((sw, sh))
display_board(win)
display_lines(win)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
