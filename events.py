"""
In file events.py processed keyboard and mouse events from user.
"""

import pygame

import constants as const


class Events():
    """
    Processed keyboard and mouse events from user.
    """

    def __init__(self, man):
        self.play = True
        self.restart = False
        self.man = man
        self.pause = False


    def work(self):
        """
        Processed input events and assigning the necessary values to
        the corresponding variables
        :return: is game continue or no
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.play = False
                elif event.key == pygame.K_r:
                    self.restart = True
                elif event.key == pygame.K_SPACE:
                    self.man.without_move = True
                elif event.key == pygame.K_p:
                    self.pause = not self.pause

                self.man.way_move = const.WAY_MOVE.get(event.key)

            if event.type == pygame.KEYUP:
                if event.key in const.WAY_MOVE.keys():
                    self.man.way_move = None
                if event.key == pygame.K_SPACE:
                    self.man.without_move = False

            keys = pygame.key.get_pressed()
            for way in const.WAY_MOVE:
                if keys[way]:
                    self.man.way_move = const.WAY_MOVE.get(way)
                    break

        return self.play
