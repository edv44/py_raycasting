import pygame
from settings import *
from map import world_map
from player import Player
from raycasting import raycasting

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit(0)

    # logic
    player.movement()

    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, player.pos, 12)
    raycasting(screen, player.pos, player.angle)

    for x, y in world_map:
        pygame.draw.rect(screen, WHITE, (x, y, TILE, TILE), 2)

    print(str(int(clock.get_fps())))
    pygame.display.flip()
    clock.tick(FPS)
