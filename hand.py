import pygame

class Hand:
    def __init__(self, *card_array):
        self.cards = list(*card_array)

    def __getattr__(self, name):
        # делегирует метод, который передается списку кард, каждой карте
        # реализация маппинга, но для методов вместо функций
        def delegate(*args, **kwargs):
            for card in self.cards:
                getattr(card, name)(*args, **kwargs)
        return delegate

    def get_cards(self):
        return self.cards

    def hide(self):
        for card in self.cards:
            # тут приходится буквально переписывать инит, так что 100% есть что-то лучше этого
            card.image = pygame.image.load('assets/card back/card_back.png')

            card.surface = pygame.Surface((card.image.get_width(), card.image.get_height()))
            card.surface.blit(card.image, (0, 0))

            card.surface = card.resize(card.image, 1 / 2)