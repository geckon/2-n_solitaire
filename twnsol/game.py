import logging
import random

import pygame

from twnsol.config import CONF
from twnsol.constants import CONST


class Game:
    """Represents the solitaire game as a whole.

    One instance of this class should be created on game start and no
    more should be needed. It stores the game state, draws the board,
    keeps the clock, etc.

    Attributes:
        display (pygame.display): the window for the game
        capt_font (pygame.font): font used for captions in the border
        state (list of lists): state of the game (columns - card values)
        next_cards (tuple): two ints representing the upcoming two cards
        clock (pygame.time.Clock): clock for the game
        score (int): current score

    """
    def __init__(self, display):
        """Initialize the game."""
        self.display = display
        pygame.font.init()
        self.capt_font = pygame.font.Font(CONST['font']['path']['default'],
                                          CONST['font']['size']['normal'])
        self.state = []
        for _ in range(CONST['column']['count']):
            self.state.append([])
        self.generate_next_cards(just_one=False)
        self.clock = pygame.time.Clock()
        self.score = 0

    def generate_next_cards(self, just_one=True):
        """Generate value(s) for the upcoming card(s).

        Mostly just one value is generated and then the next-next value
        is shifted to next and next-next is generated as a new one. If
        just_one argument is False then both values are generated anew.
        """
        if just_one:
            self.next_cards = (self.next_cards[1], get_random_card())
        else:
            self.next_cards = (get_random_card(), get_random_card())
        return self.next_cards

    def draw_border(self):
        """Draw the border around the game board.

        Draw white board around black board and add captions for score
        and the upcoming cards.
        """
        self.display.fill(CONST['color']['white'])
        pygame.draw.rect(
            self.display,
            CONST['color']['black'],
            [
                CONST['game']['border_size'],
                CONST['game']['border_size'],
                CONST['game']['height'] - 2 * CONST['game']['border_size'],
                CONST['game']['width'] - 2 * CONST['game']['border_size']
            ]
        )
        self.draw_captions()

    def draw_captions(self):
        """Draw captions for score and upcoming cards."""
        score_text = f'Score: {self.score}'
        score = self.capt_font.render(
            score_text,
            True,
            CONST['color']['black']
        )
        nc_text = f'Next cards: {self.next_cards[0]}, {self.next_cards[1]}'
        next_cards = self.capt_font.render(nc_text, True,
                                           CONST['color']['black'])
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

    def draw_cards(self, col, col_index, col_width):
        """Draw cards in a column.

        Draw cards into the specified (already drawn) column.

        Arguments:
            col (pygame.Rect): the already drawn column
            col_index (int): column index to the self.state "table"
            col_width (int): width of the column
        """
        for card_index, card in enumerate(self.state[col_index]):
            card_width = col_width - 2 * CONST['column']['space']
            card_rect = pygame.draw.rect(
                self.display,
                CONST['color']['blue'],
                [
                    col.left + CONST['column']['space'],
                    col.top + CONST['column']['space'] + card_index * (
                        CONST['card']['height'] + CONST['column']['space']
                    ),
                    card_width,
                    CONST['card']['height']
                ]
            )
            card_text = f'{card}'
            card_capt = self.capt_font.render(card_text, True,
                                              CONST['color']['white'])
            card_capt_rect = card_capt.get_rect(
                center=(
                    card_rect.left + card_width / 2,
                    card_rect.top + CONST['card']['height'] / 2
                )
            )

            logging.debug(' Card: %s', card_rect)
            logging.debug('  Card caption: %s', card_capt_rect)
            self.display.blit(card_capt, card_capt_rect)

    def draw_columns(self):
        """Draw columns and cards.

        Count column width from the board width and number of columns.
        """
        CONST['column']['space'] = 3
        border_size = CONST['game']['border_size']
        columns_cnt = CONST['column']['count']
        inner_width = CONST['game']['width'] - 2 * border_size
        col_width = (inner_width - CONST['column']['space'] *
                     (columns_cnt + 1)) / columns_cnt
        for col_index in range(columns_cnt):
            col = pygame.draw.rect(
                self.display,
                CONST['color']['green'],
                [
                    border_size + CONST['column']['space'] + col_index * (
                        col_width + CONST['column']['space']
                    ),
                    border_size + CONST['column']['space'],
                    col_width,
                    CONST['game']['height'] - 2 * (
                        border_size + CONST['column']['space']
                    )
                ]
            )
            logging.debug('Column: %s ... left %s, top %s',
                          col, col.left, col.top)

            self.draw_cards(col, col_index, col_width)

    def draw_board(self):
        """Draw border and columns including cards."""
        self.draw_border()
        self.draw_columns()
        pygame.display.update()

    def draw_game_over_screen(self):
        """Draw the game over screen.

        Black & white screen with score.
        """
        self.display.fill(CONST['color']['black'])

        go_font = pygame.font.Font(CONST['font']['path']['default'],
                                   CONST['font']['size']['big'])

        go_text = 'GAME OVER'
        go_capt = go_font.render(go_text, True, CONST['color']['white'])
        go_rect = go_capt.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['height'] * 0.25
            )
        )
        self.display.blit(go_capt, go_rect)

        score_text = f'Score: {self.score}'
        score = go_font.render(score_text, True, CONST['color']['white'])
        score_rect = score.get_rect(
            center=(
                CONST['game']['width'] / 2,
                CONST['game']['height'] * 0.75
            )
        )
        self.display.blit(score, score_rect)

        pygame.display.update()

    def game_over(self):
        """Game over.

        Display score and wait until user closes the game, then exit.
        This method does not return.
        """
        logging.info('GAME OVER')
        self.draw_game_over_screen()

        # Wait for exit
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

        # This should never happen though, since self.game_over() exits
        return True

    def squash_column(self, col):
        """ Consolidate the column.

        Merge adjacent cards with the same value (starting from the end
        of the column) and remove cards that reached the maximum value
        (set in CONSTiguration).
        """
        while len(self.state[col]) >= 1:
            # if the last card reached the maximum value
            # (and such value exists), remove the card
            if (CONF['max_card_value'] > 0 and
                    self.state[col][-1] >= CONF['max_card_value']):
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

    def process_key(self, event):
        """Process a key command from the player.

        Add the upcoming card to a respective column if the player made
        a valid turn. In such case, return True, False otherwise.
        """
        if event.key == pygame.K_1:
            logging.debug('Key 1 pressed.')
            return self.add_next_to_col(0)
        if event.key == pygame.K_2:
            logging.debug('Key 2 pressed.')
            return self.add_next_to_col(1)
        if event.key == pygame.K_3:
            logging.debug('Key 3 pressed.')
            return self.add_next_to_col(2)
        if event.key == pygame.K_4:
            logging.debug('Key 4 pressed.')
            return self.add_next_to_col(3)

        logging.debug('Unsupported key: %s', event.key)
        return False

    def loop(self):
        """The main loop.

        Draw the board and wait for the player's move. Evaluate it,
        re-draw the screen and continue until the game is finished.
        """
        while True:
            self.draw_board()
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                self.process_key(event)
            else:
                logging.debug('Unsupported event: %s', event)

        self.clock.tick(CONST['game']['fps'])


def get_random_card():
    """Generate a random card value."""
    return 2 ** random.randint(1, 6)
