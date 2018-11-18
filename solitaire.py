#!/usr/bin/env python3

import argparse
import logging
import pygame
import sys

from config import CONF
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

    # initialize and start the game
    display = pygame.display.set_mode((CONF['game']['width'],
                                       CONF['game']['height']))
    pygame.display.set_caption(CONF['game']['caption'])

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()
