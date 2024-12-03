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