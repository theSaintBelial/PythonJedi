
import pygame
from pygame.locals import *

FPS = 60

pygame.init()
pygame.display.set_mode((600, 400), RESIZABLE)
pygame.display.set_caption("На хую я вертел ваш PyGame! Ой...")
clock = pygame.time.Clock()

while True:
	clock.tick(FPS)

	for i in pygame.event.get():
		if i.type == QUIT:
			exit()

	pygame.display.update()