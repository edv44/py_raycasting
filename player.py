from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        sina = math.sin(self.angle)
        cosa = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cosa
            self.y += player_speed * sina
        if keys[pygame.K_s]:
            self.x -= player_speed * cosa
            self.y -= player_speed * sina
        if keys[pygame.K_a]:
            self.x += player_speed * sina
            self.y -= player_speed * cosa
        if keys[pygame.K_d]:
            self.x -= player_speed * sina
            self.y += player_speed * cosa
        if keys[pygame.K_RIGHT]:
            self.angle += player_angle_speed
        if keys[pygame.K_LEFT]:
            self.angle -= player_angle_speed