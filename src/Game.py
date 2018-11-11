import random

import pygame

from config import CONF


class Game:
    def __init__(self, display):
        self.display = display
        pygame.font.init()
        self.font = pygame.font.Font('./assets/Jellee-Roman/Jellee-Roman.otf',
                                     18)
        self.state = []
        for i in range(CONF['game']['card_columns']):
            self.state.append([])
        self.generate_next_cards(just_one=False)
        self.clock = pygame.time.Clock()
        self.score = 0

    def get_random_card(self):
        return 2 ** random.randint(1, 6)

    def generate_next_cards(self, just_one=True):
        if just_one:
            self.next_cards = (self.next_cards[1], self.get_random_card())
        else:
            self.next_cards = (self.get_random_card(), self.get_random_card())
        return self.next_cards

    def draw_border(self):
        self.display.fill(CONF['colors']['white'])
        pygame.draw.rect(
            self.display,
            CONF['colors']['black'],
            [
                CONF['game']['border_size'],
                CONF['game']['border_size'],
                CONF['game']['height'] - 2 * CONF['game']['border_size'],
                CONF['game']['width'] - 2 * CONF['game']['border_size']
            ]
        )
        self.draw_captions()

    def draw_captions(self):
        score_text = f'Score: {self.score}'
        score = self.font.render(score_text, True, CONF['colors']['black'])
        nc_text = f'Next cards: {self.next_cards[0]}, {self.next_cards[1]}'
        next_cards = self.font.render(nc_text, True, CONF['colors']['black'])
        next_cards_rect = next_cards.get_rect(
            center=(
                CONF['game']['width'] / 2,
                CONF['game']['height'] - CONF['game']['border_size'] / 2
            )
        )
        score_rect = score.get_rect(
            center=(
                CONF['game']['width'] / 2,
                CONF['game']['border_size'] / 2
            )
        )
        self.display.blit(score, score_rect)
        self.display.blit(next_cards, next_cards_rect)

    def draw_columns(self):
        space = 3
        border_size = CONF['game']['border_size']
        columns_cnt = CONF['game']['card_columns']
        inner_width = CONF['game']['width'] - 2 * border_size
        col_width = (inner_width - space * (columns_cnt + 1)) / columns_cnt
        card_width = col_width - 2 * space
        card_height = 50
        for col_index in range(columns_cnt):
            col = pygame.draw.rect(
                self.display,
                CONF['colors']['green'],
                [
                    border_size + space + col_index * (col_width + space),
                    border_size + space,
                    col_width,
                    CONF['game']['height'] - 2 * (border_size + space)
                ]
            )
            print(f'Column: {col} ... left {col.left}, top {col.top}')

            # draw cards in column
            for card_index, card in enumerate(self.state[col_index]):
                card_rect = pygame.draw.rect(
                    self.display,
                    CONF['colors']['blue'],
                    [
                        col.left + space,
                        col.top + space + card_index * (card_height + space),
                        card_width,
                        card_height
                    ]
                )
                card_text = f'{card}'
                card_capt = self.font.render(card_text, True,
                                             CONF['colors']['white'])
                card_capt_rect = card_capt.get_rect(
                    center=(
                        card_rect.left + card_width / 2,
                        card_rect.top + card_height / 2
                    )
                )

                print(f' Card: {card_rect}')
                print(f'  Card caption: {card_capt_rect}')
                self.display.blit(card_capt, card_capt_rect)

    def draw_screen(self):
        self.draw_border()
        self.draw_columns()
        pygame.display.update()

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
        """
        if (len(self.state[col]) >= CONF['game']['max_cards'] and
                self.state[col][-1] != self.next_cards[0]):
            # the card can't be added to this column
            return False

        # add the card
        self.state[col].append(self.next_cards[0])
        self.clock.tick(CONF['game']['fps'])
        self.draw_screen()

        # squash as many couples as possible (going from the end)
        while (len(self.state[col]) > 1):
            if self.state[col][-1] == self.state[col][-2]:
                del self.state[col][-1]
                self.score += self.state[col][-1]
                self.state[col][-1] *= 2
                self.clock.tick(CONF['game']['fps'])
                self.draw_screen()
            else:
                break

        self.generate_next_cards(just_one=True)
        return True

    def loop(self):
        self.draw_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print('Key 1 pressed.')
                        if not self.add_next_to_col(0):
                            continue
                        self.draw_screen()
                    elif event.key == pygame.K_2:
                        print('Key 2 pressed.')
                        if not self.add_next_to_col(1):
                            continue
                        self.draw_screen()
                    elif event.key == pygame.K_3:
                        print('Key 3 pressed.')
                        if not self.add_next_to_col(2):
                            continue
                        self.draw_screen()
                    elif event.key == pygame.K_4:
                        print('Key 4 pressed.')
                        if not self.add_next_to_col(3):
                            continue
                        self.draw_screen()
                    else:
                        print(f'Unsupported key: {event.key}')
                else:
                    print(f'Unsupported event: {event}')

        self.clock.tick(CONF['game']['fps'])
