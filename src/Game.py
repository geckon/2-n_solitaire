import logging
import random

import pygame

from constants import CONST


class Game:
    def __init__(self, display):
        self.display = display
        pygame.font.init()
        self.font = pygame.font.Font(CONST['font']['path']['default'],
                                     CONST['font']['size']['normal'])
        self.state = []
        for _ in range(CONST['column']['count']):
            self.state.append([])
        self.generate_next_cards(just_one=False)
        self.clock = pygame.time.Clock()
        self.score = 0

    def generate_next_cards(self, just_one=True):
        if just_one:
            self.next_cards = (self.next_cards[1], get_random_card())
        else:
            self.next_cards = (get_random_card(), get_random_card())
        return self.next_cards

    def draw_border(self):
        self.display.fill(CONST['colors']['white'])
        pygame.draw.rect(
            self.display,
            CONST['colors']['black'],
            [
                CONST['game']['border_size'],
                CONST['game']['border_size'],
                CONST['game']['height'] - 2 * CONST['game']['border_size'],
                CONST['game']['width'] - 2 * CONST['game']['border_size']
            ]
        )
        self.draw_captions()

    def draw_captions(self):
        score_text = f'Score: {self.score}'
        score = self.font.render(score_text, True, CONST['colors']['black'])
        nc_text = f'Next cards: {self.next_cards[0]}, {self.next_cards[1]}'
        next_cards = self.font.render(nc_text, True, CONST['colors']['black'])
        next_cards_rect = next_cards.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['height'] - CONST['game']['border_size'] / 2
            )
        )
        score_rect = score.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['border_size'] / 2
            )
        )
        self.display.blit(score, score_rect)
        self.display.blit(next_cards, next_cards_rect)

    def draw_columns(self):
        space = 3
        border_size = CONST['game']['border_size']
        columns_cnt = CONST['column']['count']
        inner_width = CONST['game']['width'] - 2 * border_size
        col_width = (inner_width - space * (columns_cnt + 1)) / columns_cnt
        card_width = col_width - 2 * space
        for col_index in range(columns_cnt):
            col = pygame.draw.rect(
                self.display,
                CONST['colors']['green'],
                [
                    border_size + space + col_index * (col_width + space),
                    border_size + space,
                    col_width,
                    CONST['game']['height'] - 2 * (border_size + space)
                ]
            )
            logging.debug(f'Column: {col} ... left {col.left}, top {col.top}')

            # draw cards in column
            for card_index, card in enumerate(self.state[col_index]):
                card_rect = pygame.draw.rect(
                    self.display,
                    CONST['colors']['blue'],
                    [
                        col.left + space,
                        col.top + space + card_index * (CONST['card']['height'] + space),
                        card_width,
                        CONST['card']['height']
                    ]
                )
                card_text = f'{card}'
                card_capt = self.font.render(card_text, True,
                                             CONST['colors']['white'])
                card_capt_rect = card_capt.get_rect(
                    center=(
                        card_rect.left + card_width / 2,
                        card_rect.top + CONST['card']['height'] / 2
                    )
                )

                logging.debug(f' Card: {card_rect}')
                logging.debug(f'  Card caption: {card_capt_rect}')
                self.display.blit(card_capt, card_capt_rect)

    def draw_board(self):
        self.draw_border()
        self.draw_columns()
        pygame.display.update()

    def game_over(self):
        """Game over.

        Display score and wait until user closes the game, then exit.
        This method does not return.
        """
        logging.info('GAME OVER')

        self.display.fill(CONST['colors']['black'])

        font = pygame.font.Font(CONST['font']['path']['default'],
                                CONST['font']['size']['big'])

        go_text = 'GAME OVER'
        go = font.render(go_text, True, CONST['colors']['white'])
        go_rect = go.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['height'] * 0.25
            )
        )
        self.display.blit(go, go_rect)

        score_text = f'Score: {self.score}'
        score = font.render(score_text, True, CONST['colors']['white'])
        score_rect = score.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['height'] * 0.75
            )
        )
        self.display.blit(score, score_rect)

        pygame.display.update()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()

    def check_game_over(self):
        """Check whether the game is over.

        If all the columns are full and the next upcoming card can't be
        placed on top of any of them (and merge with the current card
        on top), display the game over screen. Otherwise return False.
        """
        for col in self.state:
            if len(col) < CONST['column']['max_cards']:
                # any card can still be added
                return False

            if col[-1] == self.next_cards[0]:
                # the upcoming card can be added
                return False

        # all columns are full and not even the upcoming card can be added
        self.game_over()

    def squash_column(self, col):
        """ Consolidate the column.

        Merge adjacent cards with the same value (starting from the end
        of the column) and remove cards that reached the maximum value
        (set in CONSTiguration).
        """
        while (len(self.state[col]) >= 1):
            # if the last card reached the maximum value, remove it
            if self.state[col][-1] == CONST['card']['max_value']:
                self.score += self.state[col][-1]
                del self.state[col][-1]
                # re-draw the screen
                self.clock.tick(CONST['game']['fps'])
                self.draw_board()

            # else if the last two cards have the same value, merge them
            elif (len(self.state[col]) > 1 and
                  self.state[col][-1] == self.state[col][-2]):
                self.score += self.state[col][-1]
                del self.state[col][-1]
                self.state[col][-1] *= 2

                # re-draw the screen
                self.clock.tick(CONST['game']['fps'])
                self.draw_board()

            # otherwise we're done with squashing
            else:
                break

    def add_next_to_col(self, col):
        """Add a next card to the specified column.

        If it's possible, add it, squash the column, generate a new
        next next card and return True, otherwise return False.
        A card can be added to a column if the column is not full
        (i.e. there is less than max_cards) or if the last card in the
        column has the same value as the next card in which case it will
        be squashed next and the max_cards constraint is not violated.
        Squashing a column means merging any subsequent cards of
        the same value to one with the value doubled.
        This method will re-draw the screen (every time a card couple is
        merged plus once for the added card).
        This method also checks whether the game is over - in such case
        it won't return as the game_over() method will exit the game.
        """
        logging.debug('Adding next card (%d) to column %d',
                      self.next_cards[0], col)

        if (len(self.state[col]) >= CONST['column']['max_cards'] and
                self.state[col][-1] != self.next_cards[0]):
            # the card can't be added to this column
            return False

        # add the card
        self.state[col].append(self.next_cards[0])

        # only re-draw before squashing if there is not the extra card
        # that can only be added if it will be squashed immediately
        if len(self.state[col]) <= CONST['column']['max_cards']:
            self.clock.tick(CONST['game']['fps'])
            self.draw_board()


        self.squash_column(col)

        self.generate_next_cards(just_one=True)

        self.check_game_over()

        return True

    def loop(self):
        self.draw_board()

        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    logging.debug('Key 1 pressed.')
                    if not self.add_next_to_col(0):
                        continue
                    self.draw_board()
                elif event.key == pygame.K_2:
                    logging.debug('Key 2 pressed.')
                    if not self.add_next_to_col(1):
                        continue
                    self.draw_board()
                elif event.key == pygame.K_3:
                    logging.debug('Key 3 pressed.')
                    if not self.add_next_to_col(2):
                        continue
                    self.draw_board()
                elif event.key == pygame.K_4:
                    logging.debug('Key 4 pressed.')
                    if not self.add_next_to_col(3):
                        continue
                    self.draw_board()
                else:
                    logging.debug(f'Unsupported key: {event.key}')
            else:
                logging.debug(f'Unsupported event: {event}')

        self.clock.tick(CONST['game']['fps'])

def get_random_card():
    return 2 ** random.randint(1, 6)

