import pygame
from settings import *
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
    pygame.draw.rect(screen, AMETHYST, (0, 0, WIDTH, HEIGHT // 2))  # fill sky
    pygame.draw.rect(screen, YELLOW, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))  # fill ground
    raycasting(screen, player.pos, player.angle)

    print(str(int(clock.get_fps())))
    pygame.display.flip()
    clock.tick(FPS)
