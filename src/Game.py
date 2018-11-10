import pygame

from config import CONF

class Game:
    def __init__(self, display):
        self.display = display
        pygame.font.init()
        self.font = pygame.font.Font('./assets/Jellee-Roman/Jellee-Roman.otf', 18)
        self.cards = (
            (16,),
            (8, 4,),
            (256, 128, 32, 2),
            (32,)
        )


    def draw_border(self):
        self.display.fill(CONF['colors']['white'])
        pygame.draw.rect(self.display,
                         CONF['colors']['black'],
                         [CONF['game']['border_size'],
                          CONF['game']['border_size'],
                          CONF['game']['height'] - 2 * CONF['game']['border_size'],
                          CONF['game']['width'] - 2 * CONF['game']['border_size']])
        self.draw_captions();


    def draw_captions(self):
        self.score = 0
        score_text = f'Score: {self.score}'
        score = self.font.render(score_text, True, CONF['colors']['black'])
        next_cards = self.font.render('Next cards:', True, CONF['colors']['black'])
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
        inner_width = CONF['game']['width'] - 2 * CONF['game']['border_size']
        col_width = (inner_width - space * (CONF['game']['card_columns'] + 1)) / CONF['game']['card_columns']
        card_width = col_width - 2 * space
        card_height = 50
        for col_index in range(CONF['game']['card_columns']):
            col = pygame.draw.rect(self.display,
                                   CONF['colors']['green'],
                                   [CONF['game']['border_size'] + space + col_index * (col_width + space),
                                    CONF['game']['border_size'] + space,
                                    col_width,
                                    CONF['game']['height'] - 2 * (CONF['game']['border_size'] + space)])
            print(f'Column: {col} ... left {col.left}, top {col.top}')

            # draw cards in column
            for card_index, card in enumerate(self.cards[col_index]):
                card_rect = pygame.draw.rect(self.display,
                                             CONF['colors']['blue'],
                                             [col.left + space,
                                              col.top + space + card_index * (card_height + space),
                                              card_width,
                                              card_height])
                card_text = f'{card}'
                card_capt = self.font.render(card_text, True, CONF['colors']['white'])
                card_capt_rect = card_capt.get_rect(
                    center=(
                        card_rect.left + card_width / 2,
                        card_rect.top + card_height / 2
                    )
                )

                print(f' Card: {card_rect} ... L {card_rect.left}, T {card_rect.top}, B {card_rect.bottom}, R {card_rect.right} ')
                print(f'  Card caption: {card_capt_rect} ... L {card_capt_rect.left}, T {card_capt_rect.top}, B {card_capt_rect.bottom}, R {card_capt_rect.right}')
                print(f'  Card caption center: {(card_rect.right - card_rect.left) / 2}, {(card_rect.bottom - card_rect.top) / 2}')
                self.display.blit(card_capt, card_capt_rect)


    def draw_screen(self):
        self.draw_border()
        self.draw_columns()
        pygame.display.update()


    def loop(self):
        clock = pygame.time.Clock()
        self.draw_screen()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                #print(event)

        pygame.display.update()
        clock.tick(CONF['game']['fps'])
