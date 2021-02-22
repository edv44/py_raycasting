import pygame
import math
from settings import *
from map import world_map


def raycasting(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos

    for ray in range(NUM_RAYS):
        sina = math.sin(cur_angle)
        cosa = math.cos(cur_angle)

        for depth in range(MAX_DEPTH):
            x = xo + depth * cosa
            y = yo + depth * sina

            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                pygame.draw.line(screen, RED, player_pos, (x, y), 2)
                break
        cur_angle += DELTA_ANGLE
