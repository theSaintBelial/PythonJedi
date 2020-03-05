
import pygame

FPS = 60

pygame.init()
pygame.display.set_mode((600, 400), pygame.RESIZABLE)
clock = pygame.time.Clock()

while True:

	clock.tick(FPS)

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()

	pygame.display.update()
