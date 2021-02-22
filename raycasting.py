import pygame
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
                depth *= math.cos(player_angle - cur_angle)  # removing "fish eye"
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(screen, color, (ray * SCALE, (HEIGHT - proj_height) // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
