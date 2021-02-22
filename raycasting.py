import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def raycasting(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    xm, ym = mapping(xo, yo)

    for ray in range(NUM_RAYS):
        sina = math.sin(cur_angle)
        cosa = math.cos(cur_angle)

        # vertical collision
        x, dx = (xm + TILE, 1) if cosa >= 0 else (xm, -1)

        for i in range(0, WIDTH, TILE):
            depth_w = (x - xo) / cosa
            y = yo + depth_w * sina
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontal collision
        y, dy = (ym + TILE, 1) if sina >= 0 else (ym, -1)

        for i in range(0, HEIGHT, TILE):
            depth_h = (y - yo) / sina
            x = xo + depth_h * cosa
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        # projection
        depth = depth_w if depth_w < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)  # removing "fish eye"
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 3)
        pygame.draw.rect(screen, color, (ray * SCALE, (HEIGHT - proj_height) // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE

## OLD ALGORYTHM
# def raycasting(screen, player_pos, player_angle):
#     cur_angle = player_angle - HALF_FOV
#     xo, yo = player_pos
#
#     for ray in range(NUM_RAYS):
#         sina = math.sin(cur_angle)
#         cosa = math.cos(cur_angle)
#
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cosa
#             y = yo + depth * sina
#
#             if (x // TILE * TILE, y // TILE * TILE) in world_map:
#                 depth *= math.cos(player_angle - cur_angle)  # removing "fish eye"
#                 proj_height = PROJ_COEFF / depth
#                 c = 255 / (1 + depth * depth * 0.00002)
#                 color = (c, c // 2, c // 3)
#                 pygame.draw.rect(screen, color, (ray * SCALE, (HEIGHT - proj_height) // 2, SCALE, proj_height))
#                 break
#         cur_angle += DELTA_ANGLE
