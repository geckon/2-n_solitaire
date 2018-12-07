#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

from setuptools import setup

long_desc = """

TwN Solitaire is a simple game inspired by 2048 Solitaire (but more
generic) which is inspired by 2048 (but instead of tiles in a grid you collect
cards here). I find the game fun and satisfying and thus I decided to try and
implement it using Pygame. Here we are.

The goal of the game is to stack an endless row of cards into limited-size
columns. Each time you stack two cards of the same value one on the other,
the two cards are replaced by one of double the value and your score grows.
Cards with the maximum value (configurable, see below) will disappear.
The game ends once all the columns are full and so no more cards can be played.


CONTROLS

At the top you can see your current score, below that is the main board where
the cards are stacked. In the bottom part you can see two next cards that will
come to the game. You can use 1, 2, 3 and 4 keys to place the next upcoming
card to the respective column.


CONFIGURATION

There are some configurable options - see the default config file
(.2-n_solitaire.conf). All options should be described there including default
values which will be used if not specified otherwise. The game will search for
the configuration file in the following locations (in this order):
-   current working directory
-   home directory
-   directory specified by TWN_SOLITAIRE_CONF_DIR environment variable


Please report issues/ideas at Github.

"""

setup(
    name='twn-solitaire',
    version='0.0.1a1',
    packages=['twnsol', ],
    scripts=['solitaire.py', ],
    url='https://github.com/geckon/2-n_solitaire',
    license='GNU GPL v3',
    description='Generic version of 2048 Solitaire. Simple, fun and '
                'satisfying game.',
    long_description=long_desc,
    install_requires=[
        "pygame == 1.9.4",
        "toml == 0.10.0",
    ],
    include_package_data=True,
)
