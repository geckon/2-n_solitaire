import pygame

from config import CONF

class Game:
    def __init__(self, display):
        self.display = display

        # draw frame
        self.display.fill(CONF['colors']['white'])
        pygame.draw.rect(self.display,
                         CONF['colors']['black'],
                         [CONF['game']['frame_size'],
                          CONF['game']['frame_size'],
                          CONF['game']['height'] - 2 * CONF['game']['frame_size'],
                          CONF['game']['width'] - 2 * CONF['game']['frame_size']])

        # draw captions
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.Font('./assets/Jellee-Roman/Jellee-Roman.otf', 18)
        score_text = f'Score: {self.score}'
        score = self.font.render(score_text, True, CONF['colors']['black'])
        next_cards = self.font.render('Next cards:', True, CONF['colors']['black'])
        next_cards_rect = next_cards.get_rect(
            center=(
                CONF['game']['width'] / 2,
                CONF['game']['height'] - CONF['game']['frame_size'] / 2
            )
        )
        score_rect = score.get_rect(
            center=(
                CONF['game']['width'] / 2,
                CONF['game']['frame_size'] / 2
            )
        )
        self.display.blit(score, score_rect)
        self.display.blit(next_cards, next_cards_rect)

        # draw columns
        cards = (
            (16,),
            (8, 4,),
            (256, 128, 32, 2),
            (32,)
        )

        space = 3
        inner_width = CONF['game']['width'] - 2 * CONF['game']['frame_size']
        col_width = (inner_width - space * (CONF['game']['card_columns'] + 1)) / CONF['game']['card_columns']
        card_width = col_width - 2 * space
        card_height = 50
        for col_index in range(CONF['game']['card_columns']):
            col = pygame.draw.rect(self.display,
                                   CONF['colors']['green'],
                                   [CONF['game']['frame_size'] + space + col_index * (col_width + space),
                                    CONF['game']['frame_size'] + space,
                                    col_width,
                                    CONF['game']['height'] - 2 * (CONF['game']['frame_size'] + space)])
            print(f'Column: {col}')

            # draw cards in column
            for card_index, card in enumerate(cards[col_index]):
                card_rect = pygame.draw.rect(self.display,
                                             CONF['colors']['blue'],
                                             [col.left + space,
                                              col.top + space + card_index * (card_height + space),
                                              card_width,
                                              card_height])
                card_text = f'{card}'
                card_capt = self.font.render(card_text, True, CONF['colors']['black'])
                card_capt_rect = card_capt.get_rect(
                    center=(
                        (col.right - col.left) / 2,
                        (card_rect.bottom - card_rect.top) / 2
                    )
                )

                print(f'Card: {card_rect}')
                print(f'Card caption: {card_capt_rect}')
                self.display.blit(card_capt, card_capt_rect)





        pygame.display.update()





    def loop(self):
        clock = pygame.time.Clock()




        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                #print(event)

        pygame.display.update()
        clock.tick(CONF['game']['fps'])
