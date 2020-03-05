
import pygame

FPS = 60
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("First Fcking Try")

# немного прямоугольник:
rect = pygame.Rect(150, 100, 300, 200)
pygame.draw.rect(window, RED, rect, 10)

# немного линии:
pygame.draw.line(window, YELLOW, (20,20), (100,100), 10)
pygame.draw.aaline(window, RED, (200,200), (100,100))

# немного ломаные линии: aalines для сглаживания
pygame.draw.lines(window, WHITE, True, [(20, 20), (20, 100), (100, 100), (100, 20)], 8)

# немного полигонов (aalines для сглаживания):
pygame.draw.polygon(window, WHITE, ((300, 300), (200, 200), (200, 350), (300, 350)), 2)
pygame.draw.aalines(window, WHITE, True, ((300, 300), (200, 200), (200, 350), (300, 350)))

# немного кругов:
pygame.draw.circle(window, YELLOW, (100, 100), 50)
pygame.draw.circle(window, BLUE, (330, 330), 50, 10)

# немного эллипсов (как параметры указывается описывающий эллипс прямоугольник
pygame.draw.ellipse(window, BLUE, (100, 50, 100, 50))

# немного дуги (необходимо указывать углы начала и конца дуги в радианах)
pi = 3.14
pygame.draw.arc(window, WHITE, rect, pi, 2*pi, 3)

pygame.display.update()

while True:

	clock.tick(FPS)

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
