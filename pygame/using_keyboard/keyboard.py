import pygame

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the top"
DOWN = "to the bottom"
STOP = "stop"

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

motion = STOP

while True:
    sc.fill(BLUE)

    pygame.draw.circle(sc, WHITE, (x, y), r)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = STOP

    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    elif motion == UP:
        y -= 3
    elif motion == DOWN:
        y += 3

    clock.tick(FPS)