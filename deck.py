import pygame
import random
from card import Card

class Deck:
    def __init__(self):
        # основной список класса
        self.deck = []

        # список значений карты и цветов
        ranks = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, '2plus', 'block', 'inverse']))
        colors = ['red', 'yellow', 'green', 'blue']

        # заполняем колоду
        for color in colors:
            for rank in ranks:
                # учитываем дубли
                for _ in range(2):
                    # ВАЖНО, что создание карты происходит внутри этого цикла, а не за ним
                    card = Card(color, rank)

                    # потому что иначе эта строка создает просто ссылку на предыдущий объект
                    self.deck.append(card)

        # добавляем дикие карты
        for _ in range(4):
            wild_card_plus = Card(-1, -1, True, True)
            wild_card = Card(-1, -1, True)

            self.deck.append(wild_card)
            self.deck.append(wild_card_plus)

    def get_random_card(self):
        index = random.randint(0, len(self.deck) - 1)  # получаем индекс
        pulled_card = self.deck[index]  # вытягиваем карту
        self.deck.pop(index)  # убираем ее из колоды

        return pulled_card