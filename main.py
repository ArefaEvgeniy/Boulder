"""
File main.py use to start the game Boulder.
In this game you control a character who needs to collect a given amount of
diamonds in order to open to the next level. The character can move on empty
cells and on grass. If he steps on the grass, then the grass in this cell
disappears and in the future this cell will be empty. A stone or diamond
falls one cell down if this cell is empty. A character can move a stone if
there is an empty cell behind this stone. The character must avoid colliding
with monsters or falling on the head of a stone. In this case, the character
will die and the game will start over. The monster can be killed by throwing
a stone on its head. The monster can only move along empty cells.
"""

import pygame

import constants as const
import levels
from events import Events
from analyzer import Analyzer
from menu import Menu
from input_output import InputOutput


def main():
    """
    Main function top level to start a game, restart game, start next level
    and show information of menu.
    """

    play = True
    level = 1
    score = 0

    input_output = InputOutput(const.FILE_NAME)
    best_score = input_output.get_best_score()

    while play and levels.LEVELS.get(level):

        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.mixer.init()

        screen = pygame.display.set_mode(
            (const.WIN_WIDTH * const.SIZE + const.ADMIN_PANEL * const.SIZE,
             const.WIN_HEIGHT * const.SIZE)
        )

        menu = Menu(screen, level)
        analyzer = Analyzer(levels.LEVELS.get(level), score)

        clock = pygame.time.Clock()
        events = Events(analyzer.man)

        while play and not events.restart and not analyzer.restart:
            play = events.work()

            screen.fill(const.WHITE)

            if analyzer.run(screen, events.pause):
                score = analyzer.man.score
                level += 1

            menu.show(
                analyzer.man.score, analyzer.score_exit, best_score,
                analyzer.man.leave, events.pause, analyzer.level_complete
            )

            pygame.display.update()
            clock.tick(const.FPS)

    if score >= best_score:
        input_output.save_best_score(score)


if __name__ == "__main__":
    main()
