"""
There are maps and score for exit to next level for all levels in the file
levels.py
"""

import constants as const


LEVELS = {
    1: {
        const.AREA: [
            [6, 6, 3, 6, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 5, 5, 9],
            [4, 4, 3, 4, 4, 3, 1, 1, 1, 6, 6, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 6],
            [6, 6, 3, 6, 6, 3, 1, 1, 1, 6, 6, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3],
            [6, 6, 3, 6, 6, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 3, 6, 6],
            [6, 6, 3, 6, 6, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 6, 6],
            [4, 4, 3, 3, 3, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 4],
            [4, 4, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 4, 1, 1, 1, 3, 6, 6],
            [4, 4, 3, 1, 1, 1, 3, 3, 6, 6, 6, 1, 1, 1, 1, 1, 4, 1, 1, 3, 4, 4],
            [4, 4, 3, 1, 1, 1, 1, 3, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 4],
            [1, 3, 3, 1, 1, 4, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 4, 3, 4, 6, 6, 4, 4, 6, 6, 6, 6, 4, 5, 5, 4, 6],
            [1, 1, 1, 6, 6, 1, 4, 3, 4, 6, 6, 4, 4, 6, 6, 6, 6, 4, 6, 6, 4, 6],
            [5, 5, 1, 6, 6, 1, 1, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 6],
            [0, 5, 6, 6, 6, 6, 1, 3, 4, 4, 4, 4, 4, 6, 6, 6, 6, 4, 6, 6, 6, 6],
        ],
        const.SCORE_EXIT: 50
    },
    2: {
        const.AREA: [
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 6, 6],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6],
            [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],
            [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 5, 3, 6, 5],
            [1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 2, 5, 3, 3, 3],
            [1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 2, 3, 3, 3, 3],
            [1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 2, 5, 3, 3, 3],
            [1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 3, 3, 1, 1],
            [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 5],
            [1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 2, 5, 5, 5, 9],
        ],
        const.SCORE_EXIT: 70
    },
    3: {
        const.AREA: [
            [6, 6, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
            [6, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [6, 6, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [6, 6, 3, 1, 2, 5, 5, 8, 1, 5, 5, 8, 1, 5, 5, 8, 1, 5, 5, 8, 1, 1],
            [3, 3, 3, 1, 2, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 1],
            [1, 1, 1, 1, 2, 5, 5, 5, 1, 5, 5, 5, 1, 5, 5, 5, 1, 5, 5, 5, 1, 1],
            [1, 1, 6, 6, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
            [1, 1, 1, 4, 4, 1, 4, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
            [1, 1, 8, 1, 1, 8, 1, 8, 3, 3, 3, 3, 1, 8, 3, 5, 5, 5, 6, 5, 5, 5],
            [1, 1, 5, 1, 1, 5, 1, 5, 3, 6, 6, 3, 1, 5, 3, 5, 5, 6, 6, 6, 5, 5],
            [0, 1, 5, 1, 1, 5, 1, 5, 3, 6, 6, 3, 1, 5, 3, 5, 6, 6, 6, 6, 6, 9],
        ],
        const.SCORE_EXIT: 85
    },
    4: {
        const.AREA: [
            [6, 4, 2, 4, 6, 4, 5, 4, 6, 4, 9, 4, 6, 4, 5, 4, 6, 4, 5, 4, 6, 4],
            [1, 1, 2, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 1],
            [6, 4, 2, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 1],
            [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [6, 4, 2, 5, 5, 5, 5, 8, 5, 5, 5, 5, 5, 5, 5, 8, 5, 5, 5, 5, 5, 5],
            [1, 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [6, 4, 2, 5, 5, 8, 5, 5, 5, 8, 5, 5, 5, 8, 5, 5, 5, 8, 5, 5, 5, 8],
            [1, 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [1, 1, 2, 8, 5, 5, 5, 5, 5, 5, 5, 8, 5, 5, 5, 5, 5, 5, 5, 8, 5, 5],
            [1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2],
            [4, 4, 4, 1, 1, 4, 4, 4, 3, 1, 1, 6, 3, 1, 6, 1, 6, 3, 6, 6, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 6, 1, 3, 6, 1, 6, 1, 3, 6, 6, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 1, 3, 6, 1, 1, 3, 1, 6, 1, 6, 3, 6, 6, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 6, 1, 3, 6, 1, 6, 1, 3, 6, 6, 6, 6],
            [1, 0, 1, 1, 1, 1, 1, 1, 3, 1, 1, 6, 3, 1, 6, 1, 6, 3, 6, 6, 6, 6],
        ],
        const.SCORE_EXIT: 100
    },
    5: {
        const.AREA: [
            [9, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [5, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6],
            [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6, 7, 6, 6, 6, 6],
            [7, 6, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 6, 7, 6, 6, 6, 6],
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        ],
        const.SCORE_EXIT: 140
    },
}
