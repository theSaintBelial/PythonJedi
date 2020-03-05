
import pygame

BG_COLOR = (255, 255, 0)
COLOR1 = (255, 100, 255)
COLOR2 = (255, 0, 10)
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 600

pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Circle animation")

rad1 = 30
rad2 = 50

dx1 = 5 # speed
dy1 = 5
dx2 = 10
dy2 = 10

# in start position its beyond the window on x and in the center of it on y
x1 = rad1 + dx1
y1 = WIN_HEIGHT // 2
x2 = 100
y2 = rad2 + 10

while True:
    window.fill(BG_COLOR)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pygame.draw.circle(window, COLOR1, (x1, y1), rad1)
    pygame.draw.circle(window, COLOR2, (x2, y2), rad2)

    pygame.display.update()

    # dx is here

    if (x1 == WIN_WIDTH - rad1 or x1 == rad1):
        dx1 = -dx1
    if (x2 == WIN_WIDTH - rad2 or x2 == rad2):
        dx2 = -dx2
    if x1 + rad1 == x2 + rad2:
        dx2 = -dx2
    elif (y1 == WIN_HEIGHT - rad1 or y1 == rad1):
        dy1 = -dy1
    elif (y2 == WIN_HEIGHT - rad2 or y2 == rad2):
        dy2 = -dy2
    elif (y1 + rad1 == y2 + rad2):
        dy2 = -dy2
    x1 += dx1
    y1 += dy1

    clock.tick(FPS)