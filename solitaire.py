import pygame

from config import CONF
from src.Game import Game

def main():
    display = pygame.display.set_mode((CONF['game']['width'],
                                       CONF['game']['height']))
    pygame.display.set_caption(CONF['game']['caption'])

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()
