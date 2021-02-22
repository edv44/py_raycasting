import math

# screen settings
WIDTH = 1200
HEIGHT = 800
TILE = 100
FPS = 60
FPS_POS = WIDTH - 65, 5

# player
player_pos = (WIDTH // 2, HEIGHT // 2)
player_angle = 0
player_speed = 5
player_angle_speed = 0.05

# colors
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
AMETHYST = 100, 0, 255
SKYBLUE = 0, 186, 255
DARKGREY = 40, 40, 40
YELLOW = 255, 255, 0

# raycasting
MAX_DEPTH = 800
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 100
DELTA_ANGLE = FOV / NUM_RAYS

# 2.5d
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
