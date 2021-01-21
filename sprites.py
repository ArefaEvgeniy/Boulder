"""
There are information (images and sound) of all sprites in the file sprites.py
"""

import constants as const


SPRITES = {
    const.MAN: {
        const.IMAGES: {
            const.TOP: ['man_top.png', 'man_top1.png', 'man_top2.png'],
            const.LEFT: ['man_left.png', 'man_lef1.png', 'man_lef2.png'],
            const.RIGHT: ['man_right.png', 'man_rig1.png', 'man_rig2.png'],
            const.BOTTOM: ['man_down.png', 'man_dow1.png', 'man_dow2.png']
        },
        const.SOUND: None,
        const.SOUND_KILL: 'sounds/death man.wav',
    },
    const.ZOMBIE: {
        const.IMAGES: {
            const.TOP: ['zomb_top.png', 'zomb_top1.png', 'zomb_top2.png'],
            const.LEFT: ['zomb_left.png', 'zomb_lef1.png', 'zomb_lef2.png'],
            const.RIGHT: ['zomb_right.png', 'zomb_rig1.png', 'zomb_rig2.png'],
            const.BOTTOM: ['zomb_down.png', 'zomb_dow1.png', 'zomb_dow2.png']
        },
        const.SOUND: None,
        const.SOUND_KILL: None,
    },
    const.GRASS: {
        const.IMAGES: {const.TOP: ['grass.png']},
        const.SOUND: 'sounds/grass.wav',
        const.SOUND_KILL: 'sounds/grass.wav',
    },
    const.BRICK: {
        const.IMAGES: {const.TOP: ['brick.png']},
        const.SOUND: None,
        const.SOUND_KILL: None,
    },
    const.WALL: {
        const.IMAGES: {const.TOP: ['wall.png']},
        const.SOUND: None,
        const.SOUND_KILL: None,
    },
    const.EXIT: {
        const.IMAGES: {
            const.TOP: ['empty.png', 'exit1.png', 'exit2.png', 'exit3.png',
                        'exit4.png', 'exit5.png', 'exit6.png']
        },
        const.SOUND: 'sounds/exit.wav',
        const.SOUND_KILL: 'sounds/complete.wav',
    },
    const.EMPTY: {
        const.IMAGES: {const.TOP: ['empty.png']},
        const.SOUND: None,
        const.SOUND_KILL: None,
    },
    const.DIAMOND: {
        const.IMAGES: {
            const.TOP: ['diamond1.png', 'diamond2.png', 'diamond3.png',
                        'diamond4.png', 'diamond5.png', 'diamond6.png',
                        'diamond7.png']
        },
        const.SOUND: 'sounds/diamond.wav',
        const.SOUND_KILL: 'sounds/crash diamond.wav',
        const.SOUND_FALL: 'sounds/fall diamond.wav',
    },
    const.STONE: {
        const.IMAGES: {
            const.TOP: ['stone1.png', 'stone2.png', 'stone3.png',
                        'stone4.png', 'stone5.png']
        },
        const.SOUND: 'sounds/move stone.wav',
        const.SOUND_KILL: 'sounds/crash stone.wav',
        const.SOUND_FALL: 'sounds/fall stone.wav',
    },
    const.EXPLOSION: {
        const.IMAGES: ['empty.png', 'explos1.png', 'explos2.png',
                       'explos3.png', 'explos4.png', 'explos5.png',
                       'explos6.png', 'explos7.png', 'explos8.png'],
        const.SOUND_KILL: 'sounds/boom.wav'
    },
}
