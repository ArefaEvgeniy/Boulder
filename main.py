import pygame

import constants as const
import levels
from events import Events
from analyzer import Analyzer
from menu import Menu
from input_output import InputOutput


def main():

    play = True
    level = 1
    score = 0

    input_output = InputOutput(const.FILE_NAME)
    best_score = input_output.get_best_score()

    while play and levels.LEVELS.get(level):

        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.mixer.init()

        sc = pygame.display.set_mode(
            (const.WIN_WIDTH * const.SIZE + const.ADMIN_PANEL * const.SIZE,
             const.WIN_HEIGHT * const.SIZE)
        )

        menu = Menu(sc, level)
        analyzer = Analyzer(levels.LEVELS.get(level), score)

        clock = pygame.time.Clock()
        events = Events(analyzer.man)

        while play and not events.restart and not analyzer.restart:
            play = events.work()

            sc.fill(const.WHITE)

            if analyzer.run(sc, events.pause):
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
