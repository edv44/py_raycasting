import pygame
from settings import *
import math


def raycasting(screen, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos

    for ray in range(NUM_RAYS):
        sina = math.sin(cur_angle)
        cosa = math.cos(cur_angle)

        pygame.draw.line(screen, RED, player_pos, (xo + WIDTH * cosa, yo + WIDTH * sina), 2)
        cur_angle += DELTA_ANGLE
