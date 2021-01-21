"""
File menu.py controls the menu and massages in the game.
"""

import pygame

import constants as const


class Menu:
    """
    Show menu of the game on right side screen.
    """

    MES_SCORE = 'SCORE:'
    MES_BEST_SCORE = 'BEST SCORE:'
    MES_LEVEL = 'LEVEL {}'
    MES_P_PAUSE = 'P - pause'
    MES_RESTART = 'R - restart'
    MES_EXIT = 'ESC - exit'
    MES_SPACE = 'SPACE'
    MES_PAUSE = 'PAUSE'
    MES_COMPLETE = 'LEVEL COMPLETE'
    MES_OVER = 'GAME OVER'

    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.width = const.WIN_WIDTH * const.SIZE
        self.height = const.WIN_HEIGHT * const.SIZE
        self.admin = const.ADMIN_PANEL * const.SIZE
        self.surf_menu = None
        self.rect_menu = None
        self.diamond_image = None
        self.diamond_rect = None
        self.keys_image = None
        self.keys_rect = None
        self.init_surf()
        self.init_diamond()
        self.init_keys()


    def init_surf(self):
        """
        Show menu font.
        """
        self.surf_menu = pygame.Surface((self.admin, self.height))
        self.surf_menu.fill(const.BLACK)
        self.rect_menu = self.surf_menu.get_rect(topleft=(self.width, 0))


    def init_diamond(self):
        """
        Show diamond drawing.
        """
        self.diamond_image = (pygame.image.load('images/diamond.png')
                              .convert_alpha())
        self.diamond_image = pygame.transform.scale(
            self.diamond_image, (int(const.SIZE * 1.3), int(const.SIZE * 1.3))
        )
        self.diamond_rect = self.diamond_image.get_rect(
            center=(self.width + self.admin / 2, const.SIZE * 6)
        )


    def init_keys(self):
        """
        Show drawing of control keys.
        """
        self.keys_image = (pygame.image.load('images/keys.png')
                           .convert_alpha())
        self.keys_image = pygame.transform.scale(
            self.keys_image, (self.keys_image.get_width() // 3,
                              self.keys_image.get_height() // 3)
        )
        self.keys_rect = self.keys_image.get_rect(
            center=(self.width + self.admin / 2, const.SIZE * 9)
        )


    def show(self, score, score_exit, best_score, man_leave, pause, complete):
        """
        Show actual information on menu.
        """
        self.screen.blit(self.surf_menu, self.rect_menu)
        self.screen.blit(self.keys_image, self.keys_rect)

        UserText(self.screen, self.MES_LEVEL.format(self.level),
                 self.width + self.admin / 2, const.SIZE / 2, center=True,
                 color=const.DARK_GREEN, font=pygame.font.Font(None, 40))
        UserText(self.screen, self.MES_BEST_SCORE,
                 self.width + self.admin / 2, int(const.SIZE * 1.5),
                 font=pygame.font.Font(None, 30), center=True)
        UserText(self.screen, str(best_score), self.width + self.admin / 2,
                 const.SIZE * 2, center=True)
        UserText(self.screen, self.MES_SCORE, self.width + self.admin / 2,
                 const.SIZE * 3, center=True)
        UserText(self.screen, str(score), self.width + self.admin / 2,
                 int(const.SIZE * 3.5), center=True)
        UserText(self.screen, self.MES_SPACE, self.width + self.admin / 2,
                 (int((const.WIN_HEIGHT - 4.8) * const.SIZE)),
                 color=const.WHITE, center=True)
        UserText(self.screen, self.MES_P_PAUSE, self.width + self.admin / 2,
                 (const.WIN_HEIGHT - 3) * const.SIZE, center=True)
        UserText(self.screen, self.MES_RESTART, self.width + self.admin / 2,
                 (const.WIN_HEIGHT - 2) * const.SIZE, center=True)
        UserText(self.screen, self.MES_EXIT, self.width + self.admin / 2,
                 (const.WIN_HEIGHT - 1) * const.SIZE, center=True)

        if score_exit > 0:
            UserText(self.screen, str(score_exit),
                     self.width + self.admin / 2, const.SIZE * 5, center=True,
                     color=const.LIGHT_BLUE, font=pygame.font.Font(None, 40))
            self.screen.blit(self.diamond_image, self.diamond_rect)

        if not man_leave:
            UserText(self.screen, self.MES_OVER, self.width / 2,
                     self.height / 2, color=const.BLACK,
                     font=pygame.font.Font(None, 100), center=True)

        elif pause:
            UserText(self.screen, self.MES_PAUSE, self.width / 2,
                     self.height / 2, font=pygame.font.Font(None, 100),
                     center=True)

        elif complete:
            UserText(self.screen, self.MES_COMPLETE, self.width / 2,
                     self.height / 2, font=pygame.font.Font(None, 100),
                     center=True)


class UserText:
    """
    Show massages as "GAME OVER" in the center of screen.
    """

    def __init__(self, surf, text, x, y, color=None, font=None, center=False):
        font = font if font else pygame.font.Font(None, 32)
        color = color if color else const.YELLOW
        text = font.render(text, 1, color)

        if center:
            place = text.get_rect(center=(x, y))
        else:
            place = text.get_rect(topleft=(x, y))

        surf.blit(text, place)
