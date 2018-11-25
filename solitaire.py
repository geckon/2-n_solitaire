#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

"""
solitaire.py
------------

Executable to run the game.

Accepts -D|--debug argument to run in debug mode.
"""

import argparse
import logging
import sys

import pygame

from twnsol.config import init_config
from twnsol.constants import CONST
from twnsol.game import Game


def init_log(level=logging.WARNING):
    """Initialize log.

    WARNING is the default log level but it can be overridden.
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    logging.debug('Logging level initialized to %s', level)


def main():
    """Initialize and run the game."""
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-D', '--debug', action='store_true', dest='debug',
                        help='turn debug output on')
    args = parser.parse_args(sys.argv[1:])

    # initialize the log
    if args.debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.WARNING
    init_log(level=loglevel)

    # initialize config
    init_config()

    # initialize and start the game
    display = pygame.display.set_mode((CONST['game']['width'],
                                       CONST['game']['height']))
    pygame.display.set_caption(CONST['game']['caption'])

    game = Game(display)
    game.loop()


if __name__ == '__main__':
    main()
