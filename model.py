"""
In file model.py install models used in the game.
BaseModel - model used as base for others models.
PeopleModel - model used as base for ManModel and ZombieModel.
ManModel - model used for a character.
ZombieModel - model used for monsters.
StaticModel - model used for static objects (grass, wall, brick and exit).
DynamicModel - model used for dynamic objects (stone and diamond).
ExplosionModel - model used for a explosion.
"""

from random import randint
import pygame

import constants as const
from sprites import SPRITES


class BaseModel(pygame.sprite.Sprite):
    """
    Model used as base for other models.
    Model has variables and methods are common for all models.
    """
    IMAGES = {}
    FRAMES = {}

    def __init__(self, x_size, y_size, name, x_image=const.SIZE,
                 y_image=const.SIZE):
        pygame.sprite.Sprite.__init__(self)
        self.x_image = x_image
        self.y_image = y_image
        self.name = name
        self.counter_image = 0
        self.get_frames()
        self.image = self.FRAMES.get(const.TOP)[0]
        self.rect = self.image.get_rect(topleft=(x_size, y_size))
        self.timer = const.TIMER
        self.pause_timer = const.TIMER
        self.sound = self.get_sounds(const.SOUND)
        self.sound_kill = self.get_sounds(const.SOUND_KILL)
        self.leave = True


    def get_sounds(self, track):
        """
        Play sound.
        :param track: input track
        :return: Mixer.Sound object of pygame or None
        """
        res = None

        if SPRITES.get(self.name).get(track):
            res = pygame.mixer.Sound(SPRITES.get(self.name).get(track))

        return res


    def get_frames(self):
        """
        Show a frame.
        """
        self.FRAMES = {}
        self.IMAGES = SPRITES.get(self.name).get(const.IMAGES)


        for key in self.IMAGES:
            frames = []
            for image in self.IMAGES[key]:
                frame = pygame.image.load('{}/{}'.format(const.IMAGES, image)
                                          ).convert_alpha()
                frame = pygame.transform.scale(frame,
                                               (self.x_image, self.y_image))
                frames.append(frame)
            self.FRAMES.update({key: frames})


    def update(self):
        """
        Kill object if it's variable 'self.leave' is False.
        """
        if not self.leave:
            if self.pause():
                self.kill()


    def pause(self):
        """
        Pauses of object.
        :return: True if this object might update or move otherwise False.
        """
        res = False
        if self.pause_timer <= 0:
            res = True
            self.pause_timer = const.TIMER
        else:
            self.pause_timer -= 1
        return res


class PeopleModel(BaseModel):
    """
    Model used as base for ManModel and ZombieModel.
    Add new variables for moving and redefined 'update' method.
    """
    def __init__(self, x, y, name):
        BaseModel.__init__(self, x, y, name)
        self.way_move = None
        self.stone_push = None
        self.finish_image = self.image
        self.frames = None
        self.move = ()
        self.without_move = False


    def update(self):
        """
        Redefined method.
        Set needed image and offset for moving.
        """
        if not self.frames and self.way_move:
            self.finish_image = self.FRAMES.get(self.way_move)[0]
            self.frames = iter(self.FRAMES.get(self.way_move)[1:])

        if self.frames:
            try:
                self.image = next(self.frames)
                self.rect.x += self.move[0] * const.SIZE // 2
                self.rect.y += self.move[1] * const.SIZE // 2
            except StopIteration:
                self.frames = None

        else:
            self.image = self.finish_image


class ManModel(PeopleModel):
    """
    Model used for a character.
    Add score variable.
    """
    def __init__(self, x, y, name, score):
        PeopleModel.__init__(self, x, y, name)
        self.score = score


class ZombieModel(PeopleModel):
    """
    Model used for monsters.
    Add last_way variable so that the monster does not go back and forth.
    """
    def __init__(self, x, y, name):
        PeopleModel.__init__(self, x, y, name)
        self.last_way = const.TOP


    def update(self):
        """
        Add last_way in method.
        """
        BaseModel.update(self)
        PeopleModel.update(self)
        self.last_way = self.way_move if self.way_move else self.last_way


class StaticModel(BaseModel):
    """
    Model used for static objects (grass, wall, brick and exit).
    Add show and activate for EXIT object.
    """
    def __init__(self, x, y, name, x_image=const.SIZE, y_image=const.SIZE):
        BaseModel.__init__(self, x, y, name, x_image=x_image, y_image=y_image)
        if name == const.EXIT:
            self.go_exit = False
            self.coord = ()


    def update(self):
        """
        Add activate for EXIT object in method.
        """
        BaseModel.update(self)
        if (self.name == const.EXIT and self.go_exit
                and self.counter_image < len(self.FRAMES.get(const.TOP)) - 1):
            self.counter_image += 1
            self.image = self.FRAMES.get(const.TOP)[self.counter_image]
            self.rect = self.image.get_rect(topleft=(self.rect.x,
                                                     self.rect.y))


class DynamicModel(BaseModel):
    """
    Model used for dynamic objects (stone and diamond).
    Add moving for DIAMOND and STONE objects.
    """
    def __init__(self, x, y, name, x_image=const.SIZE, y_image=const.SIZE):
        if name == const.DIAMOND:
            x += const.SIZE // 4
            y += const.SIZE // 4
            x_image -= const.SIZE // 2
            y_image -= const.SIZE // 2

        BaseModel.__init__(self, x, y, name, x_image=x_image, y_image=y_image)

        if name == const.STONE:
            self.image = self.FRAMES.get(const.TOP)[randint(0, 4)]
            self.rect = self.image.get_rect(topleft=(x, y))
        self.push = None
        self.fall = False
        self.fall_count = 0
        self.roll_down = None
        self.sound_fall = self.get_sounds(const.SOUND_FALL)


    def update(self):
        """
        Add moving for DIAMOND and STONE objects in method.
        """
        BaseModel.update(self)

        # fall element
        if self.fall and not self.roll_down:
            self.timer -= 1

            if self.timer < 0:
                self.timer = const.TIMER
                self.fall = False
                self.fall_count += 1

            if self.timer < const.TIMER:
                self.rect.y += const.SIZE // 2

        # roll down element
        elif self.roll_down and not self.fall:
            self.timer -= 1

            if self.timer < 0:
                self.timer = const.TIMER
                self.roll_down = False
                self.fall_count += 1

            if self.timer < const.TIMER:
                self.rect.x += const.SIZE * self.roll_down // 2
                self.rect.y += const.SIZE // 2

        # turn diamond
        if self.name == const.DIAMOND:
            if self.counter_image + 1 < len(self.FRAMES.get(const.TOP)):
                self.counter_image += 1
            else:
                self.counter_image = 0
            self.image = self.FRAMES.get(const.TOP)[self.counter_image]

        # push stone
        elif self.name == const.STONE and self.push:
            if self.timer > 0:
                self.rect.x += const.MOVE[self.push][0] * const.SIZE // 2
                self.timer -= 1
            else:
                self.timer = const.TIMER
                self.push = None


class ExplosionModel(pygame.sprite.Sprite):
    """
    Model used for a explosion.
    Explosion is different from others objects so it set separately
    """
    FRAMES = []

    def __init__(self, x_size, y_size, x_image=const.SIZE,
                 y_image=const.SIZE):
        pygame.sprite.Sprite.__init__(self)
        self.x_image = x_image
        self.y_image = y_image
        self.x_size = x_size * const.SIZE
        self.y_size = y_size * const.SIZE
        self.frames = []
        self.get_frames()
        self.image = self.FRAMES[0]
        self.rect = self.image.get_rect(center=(x_size + const.SIZE / 2,
                                                y_size + const.SIZE / 2))
        self.sound_kill = pygame.mixer.Sound(
            SPRITES.get(const.EXPLOSION).get(const.SOUND_KILL)
        )
        self.start = False


    def get_frames(self):
        """
        Set frames for object.
        """
        self.FRAMES = []

        for index, image in enumerate(SPRITES.get(const.EXPLOSION)
                                      .get(const.IMAGES)):
            frame = pygame.image.load('{}/{}'.format(const.IMAGES, image)
                                      ).convert_alpha()
            factor = 1 + (index + 2 * index) / 10
            frame = pygame.transform.scale(frame,
                                           (int(self.x_image * factor),
                                            int(self.y_image * factor)))
            self.FRAMES.append(frame)


    def get_start(self, x_size, y_size):
        """
        Activate the object.
        :param x_size: x coordinate of the center object
        :param y_size: y coordinate of the center object
        :return:
        """
        self.x_size = x_size * const.SIZE
        self.y_size = y_size * const.SIZE
        self.frames = iter(self.FRAMES[1:])
        self.start = True


    def update(self):
        """
        Show next frame of object and on the end kill it.
        """
        if self.start:
            try:
                self.image = next(self.frames)
                self.rect = self.image.get_rect(
                    center=(self.x_size + const.SIZE / 2,
                            self.y_size + const.SIZE / 2)
                )
            except StopIteration:
                self.frames = None
                self.x_size = None
                self.y_size = None
                self.start = False
                self.kill()
