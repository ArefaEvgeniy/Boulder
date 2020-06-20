import pygame


WIN_WIDTH = 22
WIN_HEIGHT = 15
ADMIN_PANEL = 3
FPS = 60
FILE_NAME = 'data.txt'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)
DARK_GREEN = (0, 100, 0)
PINK = (230, 50, 230)
YELLOW = (225, 225, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
SAME_BLUE = (100, 150, 200)

SIZE = 48
GAME_SPEED = 4
TIMER = 2

TOP = 'top'
LEFT = 'left'
RIGHT = 'right'
BOTTOM = 'bottom'
RESTART = 'restart'

WAY_MOVE = {
    pygame.K_RIGHT: RIGHT,
    pygame.K_LEFT: LEFT,
    pygame.K_UP: BOTTOM,
    pygame.K_DOWN: TOP
}

AREA = 'area'
SCORE_EXIT = 'score_exit'
MAN = 'man'
ZOMBIE = 'zombie'
GRASS = 'grass'
WALL = 'wall'
BRICK = 'brick'
STONE = 'stone'
EMPTY = 'empty'
DIAMOND = 'diamond'
DIAMOND_STONE = 'diamond or stone'
EXIT = 'exit'
EXPLOSION = 'explosion'
PUSH_STONE = 'push stone'
CRASH_STONE = 'crash stone'
CRASH_DIAMOND = 'crash diamond'
DEATH_MAN = 'death man'
SPRITES = 'sprites'

IMAGES = 'images'
SOUND = 'sound'
SOUND_KILL = 'sound kill'
SOUND_FALL = 'sound fall'

NAME_BLOCK = {
    0: MAN, 1: GRASS, 2: WALL, 3: BRICK, 4: STONE, 5: EMPTY, 6: DIAMOND,
    7: DIAMOND_STONE, 8: ZOMBIE, 9: EXIT
}

MOVE = {LEFT: (-1, 0), RIGHT: (1, 0), BOTTOM: (0, -1), TOP: (0, 1)}

JSON_BEST_SCORE = "best score"
