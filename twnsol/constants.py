# -*- coding: utf-8 -*-

#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

"""
twnsol.constants
----------------

This module sets constants used by 2^n Solitaire.

CONST dictionary is provided for any module to use.
"""

import logging
import os

HERE = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(HERE, 'assets')

CONST = {
    'game': {
        'caption': '2^n Solitaire',
        'height': 500,
        'width': 500,
        'border_size': 20,
        'fps': 3,
    },
    'font': {
        'path': {
            'default': os.path.join(ASSETS_DIR,
                                    'Jellee-Roman/Jellee-Roman.otf'),
        },
        'size': {
            'normal': 18,
            'big': 36
        }
    },
    'column': {
        'space': 3,          # between columns and between cards (in px)
        'count': 4,
        'max_cards': 5,      # in a column
    },
    'card': {
        'height': 85,
        'max_value': 2048,   # then the card disappears
    },
    'color': {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (100, 0, 0),
        'green': (0, 100, 0),
        'blue': (0, 0, 100)
    }
}
