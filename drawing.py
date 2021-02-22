import pygame
from settings import *
from raycasting import raycasting


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def backgroung(self):
        pygame.draw.rect(self.screen, SKYBLUE, (0, 0, WIDTH, HEIGHT // 2))  # fill sky
        pygame.draw.rect(self.screen, DARKGREY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))  # fill ground

    def world(self, player_pos, player_angle):
        raycasting(self.screen, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, RED)
        self.screen.blit(render, (FPS_POS))
