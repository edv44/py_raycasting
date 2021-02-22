import pygame
from settings import *
from player import Player
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()
clock = pygame.time.Clock()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit(0)

    # logic
    player.movement()

    # drawing
    screen.fill(BLACK)
    drawing.backgroung()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(60)
