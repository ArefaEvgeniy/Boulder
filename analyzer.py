"""
Code in file analyzer.py analyzes behavior any sprites and behavior of game.
"""

import pygame
import time
from random import randint

import constants as const
from model import StaticModel, DynamicModel, ManModel, ZombieModel, \
    ExplosionModel


class Analyzer():
    """
    Analyze behavior any sprites and behavior of game.
    """
    SOUNDS = {}

    def __init__(self, level, score):
        self.level = level.get(const.AREA)
        self.dynamic_sprites = pygame.sprite.Group()
        self.static_sprites = pygame.sprite.Group()
        self.explosion_sprite = pygame.sprite.Group()
        self.explosion = None
        self.man = None
        self.exit = None
        self.area = {}
        self.init_sprites(score)
        self.counter = 0
        self.score_exit = level.get(const.SCORE_EXIT)
        self.sprite_fall = False
        self.level_complete = False
        self.restart = False
        self.time_start = time.monotonic()


    def init_sprites(self, score):
        """
        Create sprites on start of the level according map level.
        :param score: score of a character
        """
        self.explosion = ExplosionModel(0, 0)

        for index_y, index_x_and_name_sprite in enumerate(self.level):
            for index_x, name_sprite in enumerate(index_x_and_name_sprite):
                sprite = None
                name = const.NAME_BLOCK.get(name_sprite)
                value_x = index_x * const.SIZE
                value_y = index_y * const.SIZE
                if name == const.DIAMOND_STONE:
                    name = const.STONE if randint(0, 3) < 2 else const.DIAMOND
                if name == const.EMPTY:
                    continue
                elif name in (const.STONE, const.DIAMOND):
                    sprite = DynamicModel(value_x, value_y, name)
                    self.dynamic_sprites.add(sprite)
                elif name in (const.GRASS, const.WALL, const.BRICK):
                    sprite = StaticModel(value_x, value_y, name)
                    self.static_sprites.add(sprite)
                elif name == const.MAN:
                    self.man = ManModel(value_x, value_y, name, score)
                    sprite = self.man
                elif name == const.ZOMBIE:
                    sprite = ZombieModel(value_x, value_y, name)
                    self.dynamic_sprites.add(sprite)
                elif name == const.EXIT:
                    self.exit = StaticModel(value_x, value_y, name)
                    self.exit.coord = (index_x, index_y)
                    self.static_sprites.add(self.exit)
                    continue

                self.area[(index_x, index_y)] = sprite


    @staticmethod
    def check_coordinates(new_x, new_y):
        """
        Check new coordinates. They should not be outside of screen
        :param new_x: new x for check
        :param new_y: new y for check
        :return: True or False
        """
        res = False
        if 0 <= new_x < const.WIN_WIDTH and 0 <= new_y < const.WIN_HEIGHT:
            res = True
        return res


    def get_way(self, coordinates, area, now_way):
        """
        Definition new way for monster.
        The way of movement is randomly selected from all possible ones.
        The previous way is chosen only when there are no other possible
        paths.
        :param coordinates: current coordinates
        :param area: map of sprites on the level
        :param now_way: previous coordinates
        :return: new way
        """
        res = None
        new_x, new_y = None, None
        candidates = []
        ways = []

        # get possible ways
        for way in const.MOVE:
            new_x = coordinates[0] + const.MOVE[way][0]
            new_y = coordinates[1] + const.MOVE[way][1]
            if not self.check_coordinates(new_x, new_y):
                continue

            sprite = area.get((new_x, new_y))

            if (sprite and sprite.name in (const.STONE, const.DIAMOND)
                    and sprite.fall_count and new_x == coordinates[0]
                    and new_y == coordinates[1] - 1):
                candidates = []
                ways = []
                break

            is_man = (sprite and sprite.name == const.MAN)

            if sprite is None or is_man:
                candidates.append((new_x, new_y))
                ways.append(way)

        # remove back way if different ways are present
        if len(candidates) > 1:
            try:
                index = candidates.index(
                    (coordinates[0] - const.MOVE[now_way][0],
                     coordinates[1] - const.MOVE[now_way][1])
                )
                candidates.pop(index)
                ways.pop(index)
            except ValueError:
                pass

        if len(ways) > 0:
            index = randint(0, len(ways) - 1) if len(ways) > 1 else 0
            res = ways[index]
            new_x = candidates[index][0]
            new_y = candidates[index][1]

        return res, new_x, new_y


    def analyze_zombies(self):
        """
        Analyze behavior of monster:
            - select all sprites of monsters;
            - select new way for all monsters;
            - move all monsters;
            - kill a character if one of monsters moving to coordinates of
              character.
        """
        sprites_zombie = [
            i[0] for i in self.area.items()
            if i[1] and i[1].name == const.ZOMBIE
        ]

        for coordinates in sprites_zombie:
            elem = self.area.get(coordinates)
            elem.way_move = None
            if elem.frames is None:
                zombie_way, new_x, new_y = self.get_way(
                    coordinates, self.area, elem.last_way
                )

                # kill man
                if (self.area.get((new_x, new_y))
                        and self.area.get((new_x, new_y)).name == const.MAN):
                    self.man.sound_kill.play()
                    self.man.leave = False
                    self.restart = True

                if zombie_way:
                    elem.way_move = zombie_way
                    elem.move = const.MOVE[zombie_way]
                    self.area.pop(coordinates)
                    self.area[(new_x, new_y)] = elem


    def kill_zombie(self, x, y, area):
        """
        Kill monster of current area.
        :param x: current x.
        :param y: current y.
        :param area: current area.
        """
        if self.area.get((x, y)).leave:
            sprite = self.explosion
            self.explosion_sprite.add(sprite)
            sprite.sound_kill.play()
            sprite.get_start(x, y)

        for add_x in (-1, 0, 1):
            for add_y in (-1, 0, 1):
                new_x = x + add_x
                new_y = y + add_y

                elem = area.get((new_x, new_y))
                if elem and elem.name in (const.WALL, const.EXIT):
                    continue

                if elem:
                    area.pop((new_x, new_y))
                    elem.leave = False

                sprite = DynamicModel(
                    new_x * const.SIZE, new_y * const.SIZE, const.DIAMOND
                )
                self.dynamic_sprites.add(sprite)
                self.area[(new_x, new_y)] = sprite


    def analyze_dynamic_sprites(self):
        """
        Analyze behavior of dynamic sprite:
            - select all sprites of stone or diamond;
            - one of one action (stay, fall, crash, roll down,
              kill man or kill zombie).
        """
        sprites_is_fall = [
            i[0] for i in self.area.items()
            if i[1] and i[1].name in (const.STONE, const.DIAMOND)
        ]
        sprites_is_fall.sort(key=lambda i: i[1], reverse=True)

        for coordinates in sprites_is_fall:
            elem = self.area.get(coordinates)
            now_x = coordinates[0]
            new_y = coordinates[1] + 1

            if not self.check_coordinates(now_x, new_y):
                elem.fall_count = 0
                continue

            sprite = self.area.get((now_x, new_y))

            # fall
            if not (sprite or elem.fall or elem.roll_down or elem.push):
                self.area.pop(coordinates)
                self.area[(now_x, new_y)] = elem
                elem.fall = True

            # crash element against a brick
            elif (sprite and sprite.name == const.BRICK
                  and elem.fall and elem.fall_count > 1):
                elem.sound_kill.play()
                self.area.pop(coordinates)
                elem.leave = False
                brick = self.area.pop((now_x, new_y))
                brick.leave = False

            # roll down (left: -1, right: 1)
            elif (now_x, new_y) in sprites_is_fall:
                for direction in (-1, 1):
                    if 0 <= now_x + direction < const.WIN_WIDTH \
                        and not (self.area.get((now_x + direction, new_y - 1))
                                 or self.area.get((now_x + direction, new_y))
                                 or elem.roll_down or elem.fall or elem.push):
                        self.area.pop(coordinates)
                        self.area[(now_x + direction, new_y)] = elem
                        elem.roll_down = direction
                        break

            # kill man
            elif (sprite and sprite.name == const.MAN and not elem.fall
                  and elem.fall_count and elem.fall_count > 0):
                self.man.sound_kill.play()
                self.man.leave = False

            # kill zombie
            elif (sprite and sprite.name == const.ZOMBIE and not elem.fall
                  and elem.fall_count and elem.fall_count > 0):
                self.kill_zombie(now_x, new_y, self.area)

            # break fall_count
            if not elem.fall and elem.fall_count and sprite:
                elem.sound_fall.play()
                elem.fall_count = 0


    def analyze_man(self):
        """
        Analyze behavior of a character.
        """
        if self.man.way_move and not self.man.frames:
            add_x = const.MOVE[self.man.way_move][0]
            add_y = const.MOVE[self.man.way_move][1]
            now_x = self.man.rect.x // const.SIZE
            now_y = self.man.rect.y // const.SIZE
            new_x = now_x + add_x
            new_y = now_y + add_y

            # can't move through wall, brick or stone
            self.man.move = (0, 0)

            # level complete
            if (new_x, new_y) == self.exit.coord and self.exit.go_exit:
                self.exit.sound_kill.play()
                self.level_complete = True

            sprite = self.area.get((new_x, new_y))
            if sprite:
                # pick up grass or diamond
                if sprite.name in (const.GRASS, const.DIAMOND):
                    self.man.move = const.MOVE[self.man.way_move]
                    if sprite.name == const.DIAMOND:
                        self.man.score += 50
                        self.score_exit -= 1
                        if self.score_exit == 0:
                            self.exit.sound.play()
                            pass
                    else:
                        pass
                    sprite.leave = False
                    sprite.sound.play()
                    self.area.pop((new_x, new_y))

                # action with stone
                elif sprite.name == const.STONE:
                    condition1 = (self.man.way_move == const.RIGHT
                                  and new_x + 1 < const.WIN_WIDTH
                                  and not self.area.get((new_x + 1, new_y)))
                    condition2 = (self.man.way_move == const.LEFT
                                  and new_x - 1 >= 0
                                  and not self.area.get((new_x - 1, new_y)))

                    # push stone
                    if (not self.sprite_fall and (condition1 or condition2)
                            and not sprite.fall_count):
                        if self.man.stone_push:
                            self.man.move = const.MOVE[self.man.way_move]
                            elem = self.area.pop((new_x, new_y))
                            self.area[(new_x + add_x, new_y)] = elem
                            elem.push = self.man.way_move
                            elem.sound.play()
                            self.man.stone_push = None
                        else:
                            self.man.stone_push = (new_x, new_y)

                    else:
                        self.man.stone_push = None

                # deactivate push
                else:
                    self.man.stone_push = None

            elif self.check_coordinates(new_x, new_y):
                self.man.move = const.MOVE[self.man.way_move]

            else:
                self.man.stone_push = None

            if self.man.without_move:
                self.man.move = (0, 0)

            if self.man.move != (0, 0):
                self.area.pop((now_x, now_y))
                self.area[(new_x, new_y)] = self.man


    def run(self, screen, pause):
        """
        Main method of class. It run all methods by rotation.
        :param screen: variable of screen
        :param pause: variable of pause
        :return: True if compete or restart level otherwise False.
        """
        if self.score_exit <= 0:
            self.exit.go_exit = True

        if self.counter % const.GAME_SPEED == 0 and not pause:
            self.analyze_man()
            self.analyze_zombies()
            self.analyze_dynamic_sprites()

            self.man.update()
            self.static_sprites.update()
            self.dynamic_sprites.update()

            self.explosion_sprite.update()

            if time.monotonic() - 2 > self.time_start:
                self.time_start = time.monotonic()
                self.man.score -= 1

        self.counter += 1

        self.static_sprites.draw(screen)
        self.dynamic_sprites.draw(screen)
        self.explosion_sprite.draw(screen)
        screen.blit(self.man.image, self.man.rect)

        if not self.man.leave or self.level_complete:
            self.restart = True

        return self.level_complete
