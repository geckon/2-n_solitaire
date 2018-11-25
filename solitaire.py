#!/usr/bin/env python3

import argparse
import logging
import sys

import pygame

from config import init_config
from constants import CONST
from src.Game import Game

def init_log(level=logging.WARNING):
    """Initialize log.

    WARNING is the default log level but it can be overridden.
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    logging.debug('Logging level initialized to %s', level)


def main():
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
